import os
from flask import Flask, Response
import urllib2

app = Flask(__name__)


@app.route('/hook/payment_received')
def hook_payment_received():
    with open("status.txt", "a") as myfile:
        myfile.write("Payment Recieved")
        
    return ""


@app.route('/')
def hello():
    return 'Hello World!'