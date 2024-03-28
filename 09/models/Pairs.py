# generated by datamodel-codegen:
#   filename:  pairs_data.json
#   timestamp: 2024-03-28T15:17:43+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class ModelItem(BaseModel):
    id: str
    base_currency: str
    quote_currency: str
    quote_increment: str
    base_increment: str
    display_name: str
    min_market_funds: str
    margin_enabled: bool
    post_only: bool
    limit_only: bool
    cancel_only: bool
    status: str
    status_message: str
    trading_disabled: bool
    fx_stablecoin: bool
    max_slippage_percentage: str
    auction_mode: bool
    high_bid_limit_percentage: str


class Model(BaseModel):
    __root__: List[ModelItem]