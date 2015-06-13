# all the imports
import sqlite3
from flask import Flask, request, Response
import urllib2

app = Flask(__name__)

last_notification = ''

@app.route('/hook/payment_received', methods=['POST', ])
def hook_payment_received():
    if request.method == "POST":
        timestamp = request.form['created_at']
        id = request.form['id']

        last_notification = timestamp

    return ""


@app.route('/status')
def get_status():
    return Response(response=last_notification, mimetype="text/plain")

@app.route('/status/set/<timestamp>')
def set_status(timestamp):
    last_notification = timestamp

@app.route('/')
def hello():
    return 'Hello World!'