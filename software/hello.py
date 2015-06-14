# all the imports
from flask import Flask, request, Response, redirect, url_for, render_template
import datetime, time
import urllib2, base64
import paymill
import random

app = Flask(__name__)

last_notification = ''
last_transaction = None

paymill_tokens = ['098f6bcd4621d373cade4e832627b4f6', '12a46bcd462sd3r3care4e8336ssb4f5']
paymill_context = paymill.PaymillContext('11870062161c9d3d64f859af9746f7b5')
paymill_last_token = None
paymill_last_transaction = None

class Transaction:
    def __init__(self, timestamp, id):
        self.timestamp = timestamp
        self.id = id


@app.route('/hook/payment_received', methods=['POST', 'GET'])
def hook_payment_received():
    global last_notification, last_transaction

    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    last_notification = ts

    if request.method == "POST":
        last_transaction = Transaction(request.form['created_at'], request.form['id'])

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


@app.route('/transaction')
def transaction(amount=5):
    global paymill_last_transaction, paymill_last_token

    if paymill_last_transaction is not None:
        if time.time() - paymill_last_transaction < 30:
            new_token = paymill_last_token
            while new_token == paymill_last_token:
                new_token = random.choice(paymill_tokens)

            token = new_token
        else:
            token = paymill_last_token
    else:
        token = random.choice(paymill_tokens)

    transaction_service = paymill_context.get_transaction_service()
    try:
        transaction_with_token = transaction_service.create_with_token(
            token=token,
            amount=amount*(100 + random.randint(1,2)),
            currency='EUR',
            description='Payment'
        )
        paymill_last_transaction = time.time()
        paymill_last_token = token
        status = "OK"
    except:
        status = "FAIL"
        pass

    return Response(response=status, mimetype="text/plain")


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/<link>')
def internal_links(link):
    return render_template(link)


with app.test_request_context():
    url_for('static', filename='css/framework7.min.css')
    url_for('static', filename='css/my-app.css')
    url_for('static', filename='js/framework7.min.js')
    url_for('static', filename='js/my-app.js')
    url_for('static', filename='img/dropcare-logo.png')
