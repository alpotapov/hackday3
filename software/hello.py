# all the imports
import sqlite3
from flask import Flask, Response, request, session, g, redirect, url_for, \
     abort, render_template, flash
import urllib2

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/hook/payment_received')
def hook_payment_received():
    with open("status.txt", "a") as myfile:
        myfile.write("Payment Recieved")
        
    return ""


@app.route('/')
def hello():
    return 'Hello World!'