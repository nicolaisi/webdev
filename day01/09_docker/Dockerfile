# start by pulling the python image
FROM python:3.8-alpine

# switch working directory
WORKDIR /app

# install the dependencies
RUN python -m pip install tornado

# copy every content from the local file to the image
COPY . .

# configure the container to run in an executed manner
ENTRYPOINT [ "python", "main.py" ]