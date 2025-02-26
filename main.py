from flask import Flask

# this is used to prevent user inputs from rendering into the browser
# it was used manually to prevent injection attacks but now this is done by jinja - a template renderer in flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Zaidi's Flask Quick Start.</h1>"


@app.route('/<name>')
def path_parameters(name):
    return f'Escaping this path paramenter {escape(name)}'


@app.route('/user/<username>')
def get_user_info(username):
    return f"User info {escape(username)}"


@app.route('/post/<int:post_id>')
def get_post(post_id):
    return f"Post is {escape(post_id)}"

@app.route('/path/<path:subpath>')
def return_subpath(subpath):
    return f"Subpath is {escape(subpath)}"


