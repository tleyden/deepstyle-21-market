import flask
from flask import request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml
import json
import requests

app = flask.Flask(__name__)
payment = Payment(app, Wallet())

@app.route('/buy', methods=['POST'])
@payment.required(10000)
def deepstyle():

    # download the image contents from urls
    # JSON will look like
    # '{"style":"base64",
    #  "content":"base64"
    
    # create a JSON doc with attachment data

    # POST to sync gateway using username/password passed into CLI

    # get the doc ID and return it as the token

    return '{"token": "yNoXE"}'

@app.route('/redeem', methods=['GET'])
def deepstyle_get_result():

    # Get the document based on the token

    # If state == in progress, return json like
    # {"status": "working", "message": "Not yet finished."}
    
    # If state == finished, get image contents

    # Return image content directly
    
    # Return json URL with link to image
    
    pass


@app.route('/manifest')
def manifest():
    """
    Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)

if __name__ == "__main__":

    # need to get the username/password from the user on the
    # command line to connect to sync gw 
    
    app.debug = False
    app.run(host="0.0.0.0", port=8000)
