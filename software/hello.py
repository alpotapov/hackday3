# all the imports
from flask import Flask, request, Response, redirect, url_for, render_template
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
    return render_template("index.html")

with app.test_request_context():
    url_for('static', filename='css/framework7.min.css')
    url_for('static', filename='css/my-app.css')
    url_for('static', filename='js/framework7.min.js')
    url_for('static', filename='js/my-app.js')
