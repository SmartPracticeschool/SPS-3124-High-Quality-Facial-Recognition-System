# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:02:12 2020

@author: Tulasi
"""


from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Static content tutorial"


@app.route('/static', methods=['GET'])
def static_method():
    return render_template("static.html")  


if __name__== "__main__":
    app.run()