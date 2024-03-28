#Version pydantic: 1.10.14
from pydantic import BaseModel, Field, root_validator
from typing import Optional

class StatsModel(BaseModel):
    id: str
    base_currency: str
    quote_currency: str
    quote_increment: str
    base_increment: str  
    display_name: str
    min_market_funds: float = Field(default=0.84, description="Minimum market funds", ge=0)
    margin_enabled: bool
    post_only: bool
    limit_only: bool
    cancel_only: bool
    status: str
    status_message: str
    trading_disabled: bool
    fx_stablecoin: bool
    max_slippage_percentage: float = Field(default=0.03000000, ge=0, le=100, description="Max slippage percentage")
    auction_mode: bool
    high_bid_limit_percentage: str

    @root_validator(pre=True)
    def validate_min_market_funds(cls, values):
        if 'min_market_funds' in values and values['min_market_funds'] <= 0:
            raise ValueError('Min market funds must be greater than 0.')
        return values

    @root_validator(pre=True)
    def validate_max_slippage_percentage(cls, values):
        if 'max_slippage_percentage' in values and not 0 <= values['max_slippage_percentage'] <= 100:
            raise ValueError('Max slippage percentage must be between 0 and 100.')
        return values

    @root_validator(pre=True)
    def validate_status(cls, values):
        valid_statuses = ['active', 'inactive']
        if 'status' in values and values['status'].lower() not in valid_statuses:
            raise ValueError(f'Status must be one of {", ".join(valid_statuses)}.')
        return values

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
