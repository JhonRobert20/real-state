import pytest
from django.test import TestCase
from estates.constants import fake_estate
from fastapi.testclient import TestClient

from real_state.asgi import app
from real_state.mongodb import mongodb


@pytest.mark.django_db
class EstateEndpointsTest(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_one_estate(self):
        mongodb.remove_entire_collection()
        estate = fake_estate
        mongodb.update_many_estates([estate])
        estate_id = estate["id"]
        response = self.client.get(f"/api/estate/estates/{estate_id}")
        assert response.status_code == 200
        assert response.json() == estate
        mongodb.delete_one_estate(estate["id"])
        count_estates = len(list(mongodb.filter_estates({"_id": estate["id"]})))
        assert count_estates == 0

    def test_create_one_estate(self):
        mongodb.remove_entire_collection()
        estate = fake_estate
        response = self.client.post("/api/estate/estates/", json=estate)
        assert response.status_code == 200
        mongo_state = list(mongodb.filter_estates({"_id": estate["id"]}))
        assert mongo_state[0].get("id") == estate["id"]
        mongodb.delete_one_estate(estate["id"])
        count_estates = len(list(mongodb.filter_estates({"_id": estate["id"]})))
        assert count_estates == 0

    def test_get_all_estates(self):
        mongodb.remove_entire_collection()
        estate = fake_estate
        mongodb.update_many_estates([estate])

        response = self.client.get("/api/estate/estates/")
        assert response.status_code == 200
        assert response.json().get("total_results") == 1
        assert not response.json().get("has_next")
        assert not response.json().get("has_prev")
        assert response.json().get("pages") == 1
        assert response.json().get("page") == 1
        mongodb.remove_entire_collection()
        count_estates = len(list(mongodb.filter_estates({})))
        assert count_estates == 0
