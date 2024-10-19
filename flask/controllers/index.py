from flask import Blueprint, request, jsonify, abort, render_template
import os


index = Blueprint('index', __name__)

@index.route("/")
def home():
    return render_template('index.html')

@index.route("/testing")
def test():
    return render_template('testing.html')
