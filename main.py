import datetime
import requests
from flask import Flask, render_template

server = Flask(__name__)


@server.route("/")
def home():
    r = requests.get('https://api.npoint.io/2490efd005505d66c3d1')
    r.raise_for_status()
    return render_template("index.html",data = r.json())

@server.route("/home")
def index():
    r = requests.get('https://api.npoint.io/2490efd005505d66c3d1')
    r.raise_for_status()
    return render_template("index.html",data=r.json())

@server.route("/about")
def about():
    return render_template("about.html")

@server.route("/post/<int:value>")
def post(value):
    r = requests.get('https://api.npoint.io/2490efd005505d66c3d1')
    r.raise_for_status()
    return render_template("post.html",data=r.json(),val=value)


if __name__ == '__main__':
    server.run(debug=True)
