from flask import Flask,request, jsonify
from werkzeug.wrappers import response

import hazard_data

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/getavoid", methods = ['POST','GET'])
def get_avoid():
    print(hazard_data.areas_to_avoid())
    return "test"#hazard_data.areas_to_avoid()
