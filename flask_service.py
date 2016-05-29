import flask
from flask import request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml
import json
import requests


app = flask.Flask(__name__)
payment = Payment(app, Wallet())


@app.route('/deepstyle', methods=['POST'])
@payment.required(10000)
def deepstyle():
    return "hello"

@app.route('/manifest')
def manifest():
    """
    Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)

if __name__ == "__main__":
    app.debug = False
    app.run(host="0.0.0.0", port=8000)
