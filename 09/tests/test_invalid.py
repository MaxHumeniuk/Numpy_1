import pytest
import json
from models.Stats import StatsModel


INVALID_DATA_FILE = 'tests/invalid_data.json'


with open(INVALID_DATA_FILE, 'r') as f:
    invalid_data = json.load(f)

def test_invalid_stats_model():
    
    with pytest.raises(Exception): 
        stats_model = StatsModel(**invalid_data)
