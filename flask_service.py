import flask
from flask import request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml
import json
import requests
import buy
import sync_gateway_client

# A place to hold the connection settings for the upstream
# Sync Gateway server
sync_gateway_settings = sync_gateway_client.discover_settings()

# 21.co setup
app = flask.Flask(__name__)
payment = Payment(app, Wallet())

@app.route('/buy', methods=['POST'])
@payment.required(500000)
def deepstyle():

    json_content=request.get_json()
    job = buy.buy_request_to_job(json_content)

    sg_client = sync_gateway_client.Client(sync_gateway_settings)

    doc = sg_client.add_doc(job)
    
    # get the doc ID and return it as the token
    return buy.sync_gateway_doc_to_token(doc)


@app.route('/redeem/<token>/status', methods=['GET'])
def deepstyle_get_result_status(token):

    sg_client = sync_gateway_client.Client(sync_gateway_settings)

    doc = sg_client.get_doc(token)

    if doc["state"] == "PROCESSING_SUCCESSFUL":

        content = {'status': doc["state"]}
        return (flask.jsonify(**content), 200)

    else:
        content = {'status': doc["state"]}
        return (flask.jsonify(**content), 404)

@app.route('/redeem/<token>/image', methods=['GET'])
def deepstyle_get_result_image(token):

    sg_client = sync_gateway_client.Client(sync_gateway_settings)

    doc = sg_client.get_doc(token)

    if doc["state"] == "PROCESSING_SUCCESSFUL":

        # fetch attachment and return it
        resp = sg_client.get_doc_attachment(doc["_id"], doc["_rev"], "result_image")
        return (resp.content, resp.status_code, resp.headers.items())

    else:
        content = {'status': doc["state"]}
        return (flask.jsonify(**content), 404)
    

@app.route('/manifest')
def manifest():
    """
    Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)

if __name__ == "__main__":
    
    app.debug = True
    app.run(host="0.0.0.0", port=8001)
