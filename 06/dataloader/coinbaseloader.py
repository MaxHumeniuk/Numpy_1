import json
import pandas as pd
from datetime import datetime
from pandas.core.api import DataFrame as DataFrame
from baseloader import BaseDataLoader
from enum import Enum
import mplfinance as mpf

class Granularity(Enum):
    ONE_MINUTE=60,
    FIVE_MINUTES=300,
    FIFTEEN_MINUTES=900,
    ONE_HOUR=3600,
    SIX_HOURS=21600,
    ONE_DAY=86400

class CoinbaseLoader(BaseDataLoader):

    def __init__(self, endpoint="https://api.exchange.coinbase.com"):
        super().__init__(endpoint)

    def get_pairs(self) -> pd.DataFrame:
        data = self._get_req("/products")
        df = pd.DataFrame(json.loads(data))
        df.set_index('id', drop=True, inplace=True)
        return df

    def get_stats(self, pair: str) -> pd.DataFrame:
        data = self._get_req(f"/products/{pair}")
        return pd.DataFrame(json.loads(data), index=[0])

    def get_historical_data(self, pair: str, begin: datetime, end: datetime, granularity: Granularity) -> DataFrame:
        params = {
            "start": begin,
            "end": end,
            "granularity": granularity.value
        }

        data = self._get_req("/products/" + pair + "/candles", params)
        # parse response and create DataFrame from it
        df = pd.DataFrame(json.loads(data),
                          columns=("timestamp", "low", "high", "open", "close", "volume"))

        df.set_index('timestamp', drop=True, inplace=True)

        df.index = pd.to_datetime(df.index)
        return df

def calculate_rsa(data, window):
    return data['close'].rolling(window).mean() / data['close'].rolling(window).std()

if __name__ == "__main__":
    loader = CoinbaseLoader()
    

    all_pairs = loader.get_pairs()
    

    eth_usdt_data = loader.get_historical_data("eth-usdt", "2023-01-01", "2023-06-30", Granularity.ONE_DAY)
    btc_usdt_data = loader.get_historical_data("btc-usdt", "2023-01-01", "2023-06-30", Granularity.ONE_DAY)
    sol_usdt_data = loader.get_historical_data("sol-usdt", "2023-01-01", "2023-06-30", Granularity.ONE_DAY)
    

    print("ETH-USDT:")
    print("Mean:", eth_usdt_data['close'].mean())
    print("Standard Deviation:", eth_usdt_data['close'].std())
    print()
    
    print("BTC-USDT:")
    print("Mean:", btc_usdt_data['close'].mean())
    print("Standard Deviation:", btc_usdt_data['close'].std())
    print()
    
    print("SOL-USDT:")
    print("Mean:", sol_usdt_data['close'].mean())
    print("Standard Deviation:", sol_usdt_data['close'].std())
    print()


    print("RSA for ETH-USDT:")
    print("10-Day RSA:", calculate_rsa(eth_usdt_data, 10))
    print("20-Day RSA:", calculate_rsa(eth_usdt_data, 20))
    print("50-Day RSA:", calculate_rsa(eth_usdt_data, 50))
    print()

    print("RSA for BTC-USDT:")
    print("10-Day RSA:", calculate_rsa(btc_usdt_data, 10))
    print("20-Day RSA:", calculate_rsa(btc_usdt_data, 20))
    print("50-Day RSA:", calculate_rsa(btc_usdt_data, 50))
    print()

    print("RSA for SOL-USDT:")
    print("10-Day RSA:", calculate_rsa(sol_usdt_data, 10))
    print("20-Day RSA:", calculate_rsa(sol_usdt_data, 20))
    print("50-Day RSA:", calculate_rsa(sol_usdt_data, 50))
    print()

 
    mpf.plot(eth_usdt_data, type='candle', title='ETH-USDT')
    mpf.plot(btc_usdt_data, type='candle', title='BTC-USDT')
    mpf.plot(sol_usdt_data, type='candle', title='SOL-USDT')

