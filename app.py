from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')

def home():
    return 'Hello, World!'


app.run(host="0.0.0.0", port=80)