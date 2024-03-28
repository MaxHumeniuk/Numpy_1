import pytest
import json
from models.Stats import StatsModel


VALID_DATA_FILE = 'tests/valid_data.json'


with open(VALID_DATA_FILE, 'r') as f:
    valid_data = json.load(f)

def test_valid_stats_model():
    stats_model = StatsModel(**valid_data)
    assert stats_model
