import os
import json
import tornado.ioloop
import tornado.web
import tornado.autoreload
import tornado.gen
import tornado.web
import tornado.escape


root = os.path.dirname(__file__)

MYDATA = 0

class MainHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def options(self, *args):
        self.set_header("Access-Control-Allow-Methods", "*")
        self.set_header("Access-Control-Request-Credentials", "true")
        self.set_header("Access-Control-Allow-Private-Network", "true")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_status(204)  # No Content

    def get(self):
        data = {
            "name": "John Doe"
        }
        self.render('index.html', data=data)


class DataHandler(tornado.web.RequestHandler):

    def _return_response(self, request, message_to_be_returned: dict, status_code):
        """
        Returns formatted response back to client
        """
        try:
            request.set_header("Content-Type", "application/json; charset=UTF-8")
            request.set_status(status_code)

            #If dictionary is not empty then write the dictionary directly into
            if(bool(message_to_be_returned)):
                request.write(message_to_be_returned)

            request.finish()
        except Exception:
            raise

    def set_default_headers(self, *args, **kwargs):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "*")

    def put(self):
        """
        This function parses the request body and does something
        """
        global MYDATA
        try:
            # Do something with request body
            request_payload = tornado.escape.json_decode(self.request.body)
            MYDATA = request_payload["data"]
            print("Stored value " + str(MYDATA))
            return self._return_response(self, request_payload, 200)

        except json.decoder.JSONDecodeError:
            return self._return_response(self, { "message": 'Cannot decode request body!' }, 400)

        except Exception as ex:
            return self._return_response(self, { "message": 'Could not complete the request because of some error at the server!', "cause": ex.args[0], "stack_trace": traceback.format_exc(sys.exc_info()) }, 500)

    def get(self):
        global MYDATA
        self.write({"data": MYDATA})


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/data/", DataHandler),
], debug=True, static_path=os.path.join(root, 'static'),
    cookie_secret='L8LwECiNRxq2N0N2eGxx9MZlrpmuMEimlydNX/vt1LM=')


if __name__ == "__main__":
    application.listen(8888)
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.instance().start()
