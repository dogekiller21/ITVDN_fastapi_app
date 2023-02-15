from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app
from app.config import DATABASE_URL


class APITestCase(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_main_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        # TODO: Желательно другую базу юзать
        user_data = {
            "user": {
                "email": "test999@test.com",
                "password": "123",
                "first_name": "FN",
                "last_name": "LN",
                "username": "UN"
            }
        }
        response = self.client.post("/user", json=user_data)
        self.assertEqual(response.status_code, 200)
