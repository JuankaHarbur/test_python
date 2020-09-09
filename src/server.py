from flask import Flask
server = Flask(__name__)


@server.route("/")
def hello():
    return "Hello World!x"


if __name__ == "__main__":
    server.run()
