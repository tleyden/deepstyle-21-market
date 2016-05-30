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
## @payment.required(10000)
def deepstyle():

    json_content=request.get_json()
    print("json: {} type: {}".format(json_content, type(json_content)))
    job = buy.buy_request_to_job(json_content)
    print("job keys: {}".format(job.keys()))

    # POST to sync gateway using username/password passed into CLI
    sg_client = sync_gateway_client.Client(sync_gateway_settings)

    print("adding doc")
    doc = sg_client.add_doc(job)
    
    print("doc: {}".format(doc))
    
    # get the doc ID and return it as the token
    return buy.sync_gateway_doc_to_token(doc)


@app.route('/redeem/<token>', methods=['GET'])
def deepstyle_get_result(token):

    print("token: {}".format(token))

    sg_client = sync_gateway_client.Client(sync_gateway_settings)

    doc = sg_client.get_doc(token)

    print("doc: {}".format(doc))

    if doc["state"] == "PROCESSING_SUCCESSFUL":

        # fetch attachment and return it
        resp = sg_client.get_doc_attachment(doc["_id"], doc["_rev"], "result_image")
        return (resp.content, resp.status_code, resp.headers.items())

    else:
        content = {'status': doc["state"]}
        return content, status.HTTP_404_NOT_FOUND



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
    app.run(host="0.0.0.0", port=8000)
