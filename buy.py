
import base64
import urllib.request

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
        attachments["content_image"] = {
            "data": download_and_base64(buy_dictionary["content_image_url"])
        }
    if "style_image_base64_data" in buy_dictionary:
        attachments["style_image"] = {
            "data": buy_dictionary["style_image_base64_data"]
        }
    if "content_image_base64_data" in buy_dictionary:
        attachments["content_image"] = {
            "data": buy_dictionary["content_image_base64_data"]
        }
        
    result["_attachments"] = attachments
    return result


def download_and_base64(image_url):
    
    with urllib.request.urlopen(image_url) as url:
        raw_content = url.read()
        content_base64 = base64.standard_b64encode(raw_content)
        return content_base64
