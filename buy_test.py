import unittest
import buy

class BuyTestUrls(unittest.TestCase):

    def test(self):

        data = {
            "style_image_url": "http://tleyden-misc.s3.amazonaws.com/21style/van_gogh.jpg",
            "content_image_url": "http://tleyden-misc.s3.amazonaws.com/21style/backyard.jpg"
        }
        result = buy.buy_request_to_job(data)
        self.assertEqual(result["state"], "READY_TO_PROCESS")
        self.assertEqual(result["type"], "job")
        attachments = result["_attachments"]
        self.assertEqual(len(attachments), 2)
        style_image_data = attachments["style_image"]["data"]
        content_image_data = attachments["content_image"]["data"]
        self.assertTrue(len(style_image_data) > 0)
        self.assertTrue(len(content_image_data) > 0)


class BuyTestBase64Data(unittest.TestCase):

    def test(self):

        data = {
            "style_image_base64_data": "ljlkjkj",
            "content_image_base64_data": "lkjlkjlkj"
        }
        result = buy.buy_request_to_job(data)
        self.assertEqual(result["state"], "READY_TO_PROCESS")
        self.assertEqual(result["type"], "job")
        attachments = result["_attachments"]
        self.assertEqual(len(attachments), 2)
        style_image_data = attachments["style_image"]["data"]
        content_image_data = attachments["content_image"]["data"]
        self.assertTrue(len(style_image_data) > 0)
        self.assertTrue(len(content_image_data) > 0)
        

if __name__ == '__main__':
    unittest.main()
