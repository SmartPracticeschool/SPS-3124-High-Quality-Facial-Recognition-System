# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11 2020

@author: Shyam sunder Reddy
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "This site is  novel"

@app.route('/getname',methods=["GET"])
def get_name() ->str:
    return "Shyam"


@app.route('/name/<name>',methods=["GET"])
def name(name):
    return "Hello %s " % name

@app.route('/age/<int:age>',methods=["GET"])
def get_age(age):
    return "your age is %d " %age


if__name__= '__main__'
app.run()
