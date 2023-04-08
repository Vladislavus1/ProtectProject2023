import unittest
import requests


class TestCalendarAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:5000"
        self.header = {"Content-type": "Application/json"}
        self.login_data = {
            "username": ""
        }

    def test1_login(self):
        response = requests.post(f"{self.url}/login", json=self.login_data, headers=self.header)

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

