# all the imports
from flask import Flask, request, Response, redirect, url_for, render_template
import datetime, time
import urllib2, base64
import paymill

app = Flask(__name__)

last_notification = ''
last_transaction = None

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
@app.route('/transaction/<token>')
def transaction(amount=5, token="098f6bcd4621d373cade4e832627b4f6"):
    paymill_context = paymill.PaymillContext('11870062161c9d3d64f859af9746f7b5')

    # payment_service = paymill_context.get_payment_service()
    # payment_with_token = payment_service.create()
    # token='12a46bcd462sd3r3care4e8336ssb4f5'

    transaction_service = paymill_context.get_transaction_service()
    transaction_with_token = transaction_service.create_with_token(
        token=token,
        amount=amount*100,
        currency='EUR',
        description='Payment'
    )

    return ""


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
