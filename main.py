import datetime
import requests
from flask import Flask, render_template, request, redirect, url_for

server = Flask(__name__)


@server.route("/")
def home():
    r = requests.get('https://api.npoint.io/2490efd005505d66c3d1')
    r.raise_for_status()
    date = datetime.datetime.now().year
    return render_template("index.html", data=r.json(), curr_date=date)


@server.route("/home")
def index():
    r = requests.get('https://api.npoint.io/2490efd005505d66c3d1')
    r.raise_for_status()
    date = datetime.datetime.now().year
    return render_template("index.html", data=r.json(), curr_date=date)


@server.route("/about")
def about():
    return render_template("about.html")


@server.route("/post/<int:value>")
def post(value):
    r = requests.get('https://api.npoint.io/2490efd005505d66c3d1')
    r.raise_for_status()
    print(value)
    return render_template("post.html", data=r.json(), val=value)


@server.route("/contact")
def contact():
    return render_template("contact.html",h1= 'Contact me',span='Have questions? I have answers.')


@server.route("/contact-login",methods=['POST'])
def contact_form():
    if request.method == "POST":
        return render_template('contact.html',h1='Successfully sent!!',span='')
    else:
        return 'error'



# @server.route("/form")
# def form():
#     return render_template("index_form.html")
#
#
# '''Form Handling where we are getting the data from the form and displaying it on the page itself (use the /login
# route to see the form in action and send the username and password using request to "index_form_success.html"
#  for displaying) '''
#
#
# @server.route("/login", methods=['POST'])
# def login():
#     if request.method == 'POST':
#         user = request.form['name']
#         password = request.form['password']
#         return render_template('index_form_success.html', username=user, password=password)
#     else:
#         return "Invalid Request Method"


if __name__ == '__main__':
    server.run(debug=True)
