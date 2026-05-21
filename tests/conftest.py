import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


def _reset_activities():
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))


@pytest.fixture
def client():
    _reset_activities()
    with TestClient(app) as test_client:
        yield test_client
