from flask import Blueprint, render_template


index = Blueprint('index', __name__)


@index.route("/")
def home():
    return render_template('index.html')


@index.route("/testing")
def test():
    return render_template('testing.html')
