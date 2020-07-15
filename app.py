#! /use/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world"

@app.route("/david")
def david():
  return "Hello, david"

@app.route("/maria")
def maria():
  return "Hello, maria"
