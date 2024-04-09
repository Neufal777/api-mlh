import requests
import unittest

import requests
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8000"
        self.admin_credentials = ("Pranav", "pass")
        self.user_credentials = ("Kosu", "pass")
        self.invalid_credentials = ("Invalid", "InvalidPass")
    
    def test_authentication_success(self):
        print("Testing authentication success")
        print(self.base_url)
        response = requests.get(f'{self.base_url}/users', auth=self.admin_credentials)
        self.assertEqual(response.status_code, 200)
    
    def test_authentication_failure(self):
        print("Testing authentication failure")
        response = requests.get(f'{self.base_url}/users', auth=self.invalid_credentials)
        self.assertEqual(response.status_code, 401)

    def test_authorization_failure(self):
        print("Testing authorization failure")
        response = requests.get(f'{self.base_url}/users', auth=self.user_credentials)
        self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
    unittest.main()
