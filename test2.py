# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 2020

@author: Shyam sunder Reddy
"""
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("test.html")


@app.route('/dashboard/<name>', methods=['GET'])
def dashboard(name):
    return render_template("dashboard.html",user_name=name)  


if __name__== "__main__":
    app.run()