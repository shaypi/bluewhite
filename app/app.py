import unittest
from flask import Flask
import socket
from urllib.parse import urlsplit

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_get_hostname(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hostname:', response.data.decode())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
