import json
from datetime import datetime
from enum import Enum
import asyncio
import logging
import time

from .baseloader import BaseDataLoader

class Granularity(Enum):
    ONE_MINUTE = 60
    FIVE_MINUTES = 300
    FIFTEEN_MINUTES = 900
    ONE_HOUR = 3600
    SIX_HOURS = 21600
    ONE_DAY = 86400

class CoinbaseLoader(BaseDataLoader):

    def __init__(self, endpoint="https://api.exchange.coinbase.com"):
        super().__init__(endpoint)
        self._logger = logging.getLogger("COINBASE")
        self._logger.info("created")

    async def get_pairs(self) -> dict[str, any]:
        self._logger.debug("get pairs")
        start_time = time.time()
        data = await self._get_req("/products")
        end_time = time.time()
        self._logger.info(f"Time for GET /products (non-blocking IO): {end_time - start_time} seconds")
        return json.loads(data)
    
    async def get_stats(self, pair: str) -> dict[str, any]:
        self._logger.debug(f"get pair {pair} stats")
        start_time = time.time()
        data = await self._get_req(f"/products/{pair}")
        end_time = time.time()
        self._logger.info(f"Time for GET /products/{pair} (non-blocking IO): {end_time - start_time} seconds")
        return json.loads(data)

    async def get_historical_data(self, pair: str, begin: datetime, end: datetime, granularity: Granularity) -> dict[str, any]:
        self._logger.debug(f"get pair {pair} history")
        start_time = time.time()
        params = {
            "start": begin,
            "end": end,
            "granularity": granularity.value
        }
        data = await self._get_req("/products/" + pair + "/candles", params)
        end_time = time.time()
        self._logger.info(f"Time for GET /products/{pair}/candles (non-blocking IO): {end_time - start_time} seconds")
        return json.loads(data)

    async def get_data_history(self, pairs: list[str], begin: datetime, end: datetime, granularity: Granularity) -> dict[str, any]:
        self._logger.debug(f"get history for pairs: {pairs}")
        start_time = time.time()
        tasks = [self.get_historical_data(pair, begin, end, granularity) for pair in pairs]
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        self._logger.info(f"Time for multiple requests (non-blocking IO): {end_time - start_time} seconds")
        return {
            "async_results": results
        }

async def main():
    logging.basicConfig(level=logging.INFO)
    loader = CoinbaseLoader()
    pairs = await loader.get_pairs()
    print("Pairs:", pairs)
    stats = await loader.get_stats("btc-usdt")
    print("Stats for BTC-USDT:", stats)
    historical_data = await loader.get_historical_data("btc-usdt", "2023-01-01", "2023-06-30", granularity=Granularity.ONE_DAY)
    print("Historical Data for BTC-USDT:", historical_data)
    data_history = await loader.get_data_history(["btc-usdt", "eth-usdt"], "2023-01-01", "2023-06-30", granularity=Granularity.ONE_DAY)
    print("Data History for BTC-USDT and ETH-USDT:")
    print("Async Results:", data_history["async_results"])

if __name__ == "__main__":
    asyncio.run(main())
