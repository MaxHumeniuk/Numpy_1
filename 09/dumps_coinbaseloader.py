from dataloader.coinbaseloader import CoinbaseLoader
from dataloader.coinbaseloader import Granularity
import json

loader = CoinbaseLoader()

pairs_data = loader.get_pairs()
with open('pairs_data.json', 'w') as f:
    json.dump(pairs_data, f)

if pairs_data:
    first_pair = pairs_data[0]['id']
    stats_data = loader.get_stats(pair=first_pair)
    with open('stats_data.json', 'w') as f:
        json.dump(stats_data, f)

historical_data = loader.get_historical_data(pair=first_pair, begin='2023-01-01', end='2023-06-30', granularity=Granularity.ONE_DAY)
with open('historical_data.json', 'w') as f:
    json.dump(historical_data, f)
