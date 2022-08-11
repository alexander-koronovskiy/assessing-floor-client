import json

import pytest
import falcon

from main import create_app, get_config


class TestSolrProvider:

    @pytest.fixture
    def client(self):
        config = get_config()
        app = create_app(config)
        return falcon.testing.TestClient(app)

    @staticmethod
    def _load_valid_response():
        with open(pytest.valid_response_path, 'r') as json_file:
            return json.load(json_file)

    @staticmethod
    def _load_correct_plan():
        with open(pytest.correct_plan_path, 'rb') as image_file:
            return image_file.read()

    def test_list_images(self):
        resp = self.client.simulate_get('/images')
        assert resp.status_code == 200
        assert resp.json == []
