import unittest
from unittest.mock import patch
from flask import Flask
from app.api.sample_controller import get_greeting, create_greeting

class SampleControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.route('/api/v1/sample', methods=['GET'])(get_greeting)
        self.app.route('/api/v1/sample', methods=['POST'])(create_greeting)
        self.client = self.app.test_client()

    @patch('api.sample_controller.some_external_dependency')
    def test_get_greeting(self, mock_dependency):
        # Mock the external dependency behavior
        mock_dependency.return_value = "mocked response"

        response = self.client.get('/api/v1/sample')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

    @patch('api.sample_controller.some_database_call')
    def test_create_greeting(self, mock_database_call):
        # Mock the database call behavior
        mock_database_call.return_value = True

        response = self.client.post('/api/v1/sample', json={"name": "Alice"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Hello, Alice!"})

        # Test with missing name field
        response = self.client.post('/api/v1/sample', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Invalid input data."})

if __name__ == '__main__':
    unittest.main()
