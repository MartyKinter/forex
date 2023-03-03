from unittest import TestCase
from app import app


class TestForex(TestCase):
    
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        
    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Supported currencies", response.data)
        
    def test_valid_conversion(self):
        data = {"convert-from": "USD", "convert-to": "EUR", "amount": "100"}
        response = self.client.post("/result", data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"result is", response.data)
        
    def test_invalid_conversion(self):
        data = {"convert-from": "USD", "convert-to": "XXX", "amount": "100"}
        response = self.client.post("/result", data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Not a valid", response.data)
    
    def test_invalid_amount(self):
        data = {"convert-from": "USD", "convert-to": "EUR", "amount": "XXX"}
        response = self.client.post("/result", data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Not a valid", response.data)

    def test_usd_to_usd_conversion(self):
        data = {"convert-from": "USD", "convert-to": "USD", "amount": "1"}
        response = self.client.post("/result", data=data, follow_redirects=True)
        self.assertIn(b'result is 1', response.data)