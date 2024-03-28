import pytest
import json
from models.Stats import StatsModel

# Шлях до JSON-файлу з невалідними даними
INVALID_DATA_FILE = 'tests/invalid_data.json'

# Зчитуємо дані з JSON-файлу з невалідними даними
with open(INVALID_DATA_FILE, 'r') as f:
    invalid_data = json.load(f)

def test_invalid_stats_model():
    # Перевірка невалідних даних
    with pytest.raises(Exception):  # Змініть тип помилки, якщо він відрізняється від загального Exception
        stats_model = StatsModel(**invalid_data)
