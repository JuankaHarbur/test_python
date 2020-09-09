from flask import Flask
server = Flask(__name__)


@server.route("/")
def hello():
    return "Hello World! nuevo"


if __name__ == "__main__":
    server.run()
