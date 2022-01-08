from flask import Flask
import hazard_data

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/avoid")
def get_avoid():
    return hazard_data.areas_to_avoid()
