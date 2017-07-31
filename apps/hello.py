# -*- coding=utf-8 -*-
"""
test index page
create by paddy.guan
"""
from flask import Flask


app = Flask(__name__)


app.route('/')
def index():
    return r'<html><h1>Hello Page!!</html>'
