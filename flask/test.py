#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Drink more coffee Right Now!"

app.run(host="0.0.0.0", port=5000)