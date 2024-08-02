from flask import Flask
from routes.ping import ping

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


app.add_url_rule("/ping", view_func=ping, methods=["GET"])
