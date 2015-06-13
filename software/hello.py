# all the imports
from flask import Flask, request, Response, redirect
import datetime, time

app = Flask(__name__)

last_notification = ''

@app.route('/hook/payment_received', methods=['POST', 'GET'])
def hook_payment_received():
    global last_notification

    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    last_notification = ts

    # if request.method == "POST":
    #     timestamp = request.form['created_at']
    #     id = request.form['id']
    #
    #     last_notification = timestamp

    return ""


@app.route('/status')
def get_status():
    if last_notification == '':
        status = 'No data'
    else:
        status = last_notification
    return Response(response=status, mimetype="text/plain")

@app.route('/status/set/<timestamp>')
def set_status(timestamp):
    global last_notification
    last_notification = timestamp
    return redirect('/status')

@app.route('/')
def hello():
    return '!Hello World!'