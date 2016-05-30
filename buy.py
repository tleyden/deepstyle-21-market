
import base64
import urllib.request
import json

def buy_request_to_job(buy_dictionary):
    """
    Given a dictionary of Buy parameters, convert this to a
    DeepStyle Job that can be posted to Sync Gateway
    """

    result = {
        "state": "READY_TO_PROCESS",
        "type": "job"
    }

    attachments = {}
    if "style_image_url" in buy_dictionary:
        attachments["style_image"] = {
            "data": download_and_base64(buy_dictionary["style_image_url"])
        }
    if "content_image_url" in buy_dictionary:
        attachments["source_image"] = {
            "data": download_and_base64(buy_dictionary["content_image_url"])
        }
    if "style_image_base64_data" in buy_dictionary:
        attachments["style_image"] = {
            "data": buy_dictionary["style_image_base64_data"]
        }
    if "content_image_base64_data" in buy_dictionary:
        attachments["source_image"] = {
            "data": buy_dictionary["content_image_base64_data"]
        }
        
    result["_attachments"] = attachments
    return result


def sync_gateway_doc_to_token(doc):
    """
    Given the document returned from sync gateway:

    {'id': '00d9d307d509eb9ce9423c4c210eb88e', 'rev': '1-a84d65867c75df30d02aaa8307af5476', 'ok': True}

    Return a json serialized doc with a token field with the doc id:

    {'token': '00d9d307d509eb9ce9423c4c210eb88e'}

    """
    json_dict = {
        "token": doc["id"]
    }
    return json.dumps(json_dict)
    

def download_and_base64(image_url):
    
    with urllib.request.urlopen(image_url) as url:
        raw_content = url.read()
        content_base64 = base64.standard_b64encode(raw_content)
        return content_base64.decode()
