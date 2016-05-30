import os
import requests
import json
from requests.auth import HTTPBasicAuth

DEEPSTYLE_SYNC_GATEWAY_URL = "DEEPSTYLE_SYNC_GATEWAY_URL"
DEEPSTYLE_SYNC_GATEWAY_DB = "DEEPSTYLE_SYNC_GATEWAY_DB" 
DEEPSTYLE_SYNC_GATEWAY_USERNAME = "DEEPSTYLE_SYNC_GATEWAY_USERNAME"
DEEPSTYLE_SYNC_GATEWAY_PASSWORD = "DEEPSTYLE_SYNC_GATEWAY_PASSWORD" 

class Client:

    def __init__(self, settings):
        self.settings = settings
        self.url = settings[DEEPSTYLE_SYNC_GATEWAY_URL]
        self.db = settings[DEEPSTYLE_SYNC_GATEWAY_DB]
        self.username = settings[DEEPSTYLE_SYNC_GATEWAY_USERNAME]
        self.password = settings[DEEPSTYLE_SYNC_GATEWAY_PASSWORD]
        self.headers = {'Content-Type': 'application/json'}

    def add_doc(self, doc):

        print("going to serialize doc")
        body = json.dumps(doc)
        print("serialized doc, body len: {}", len(body))
        
        resp = requests.post(
            "{0}/{1}/".format(self.url, self.db),
            auth=HTTPBasicAuth(self.username, self.password),
            headers=self.headers,
            data=body
        )
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json
        

def discover_settings():

    settings = {}
    
    if DEEPSTYLE_SYNC_GATEWAY_URL in os.environ:
        settings[DEEPSTYLE_SYNC_GATEWAY_URL] = os.environ[DEEPSTYLE_SYNC_GATEWAY_URL]
    else:
        raise Exception("You must define the environment variable: {}".format(DEEPSTYLE_SYNC_GATEWAY_URL))

    if DEEPSTYLE_SYNC_GATEWAY_USERNAME in os.environ:
        settings[DEEPSTYLE_SYNC_GATEWAY_USERNAME] = os.environ[DEEPSTYLE_SYNC_GATEWAY_USERNAME]
    else:
        raise Exception("You must define the environment variable: {}".format(DEEPSTYLE_SYNC_GATEWAY_USERNAME))

    if DEEPSTYLE_SYNC_GATEWAY_PASSWORD in os.environ:
        settings[DEEPSTYLE_SYNC_GATEWAY_PASSWORD] = os.environ[DEEPSTYLE_SYNC_GATEWAY_PASSWORD]
    else:
        raise Exception("You must define the environment variable: {}".format(DEEPSTYLE_SYNC_GATEWAY_PASSWORD))

    if DEEPSTYLE_SYNC_GATEWAY_DB in os.environ:
        settings[DEEPSTYLE_SYNC_GATEWAY_DB] = os.environ[DEEPSTYLE_SYNC_GATEWAY_DB]
    else:
        raise Exception("You must define the environment variable: {}".format(DEEPSTYLE_SYNC_GATEWAY_DB))

    
    return settings
