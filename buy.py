import urllib
import base64

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
    if buy_dictionary.has_key("style_image_url"):
        attachments["style_image"] = {
            "data": download_and_base64(buy_dictionary["style_image_url"])
        }
    if buy_dictionary.has_key("content_image_url"):
        attachments["content_image"] = {
            "data": download_and_base64(buy_dictionary["content_image_url"])
        }

    result["_attachments"] = attachments
    return result


def download_and_base64(image_url):
    f = urllib.urlopen(image_url)
    raw_content = f.read()
    content_base64 = base64.standard_b64encode(raw_content)
    return content_base64
