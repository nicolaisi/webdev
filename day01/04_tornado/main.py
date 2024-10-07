import os
import tornado.ioloop
import tornado.web
import tornado.autoreload


root = os.path.dirname(__file__)


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


class GetDataHandler(tornado.web.RequestHandler):
    def get(self):
        data = {
            "value": 10
        }
        self.write(data)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/getdata/?", GetDataHandler), # get data from cache file
], debug=True, static_path=os.path.join(root, 'static'),
    cookie_secret='L8LwECiNRxq2N0N2eGxx9MZlrpmuMEimlydNX/vt1LM=')


if __name__ == "__main__":
    application.listen(8888)
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.instance().start()
