import pytest
from models.Stats import StatsModel

# Тест для перевірки валідації min_market_funds
def test_min_market_funds_validation():
    with pytest.raises(ValueError):
        StatsModel(
            id="GALA-EUR",
            base_currency="GALA",
            quote_currency="EUR",
            quote_increment="0.0001",
            base_increment="1",
            display_name="GALA-EUR",
            min_market_funds=-1,  # Невалідне значення
            margin_enabled=False,
            post_only=False,
            limit_only=False,
            cancel_only=False,
            status="delisted",
            status_message="",
            trading_disabled=True,
            fx_stablecoin=False,
            max_slippage_percentage="0.03000000",
            auction_mode=False,
            high_bid_limit_percentage=""
        )

# Тест для перевірки валідації max_slippage_percentage
def test_max_slippage_percentage_validation():
    with pytest.raises(ValueError):
        StatsModel(
            id="GALA-EUR",
            base_currency="GALA",
            quote_currency="EUR",
            quote_increment="0.0001",
            base_increment="1",
            display_name="GALA-EUR",
            min_market_funds=0.84,
            margin_enabled=False,
            post_only=False,
            limit_only=False,
            cancel_only=False,
            status="delisted",
            status_message="",
            trading_disabled=True,
            fx_stablecoin=False,
            max_slippage_percentage=101,  # Невалідне значення
            auction_mode=False,
            high_bid_limit_percentage=""
        )

# Тест для перевірки валідації status
def test_status_validation():
    with pytest.raises(ValueError):
        StatsModel(
            id="GALA-EUR",
            base_currency="GALA",
            quote_currency="EUR",
            quote_increment="0.0001",
            base_increment="1",
            display_name="GALA-EUR",
            min_market_funds=0.84,
            margin_enabled=False,
            post_only=False,
            limit_only=False,
            cancel_only=False,
            status="invalid_status",  # Невалідне значення
            status_message="",
            trading_disabled=True,
            fx_stablecoin=False,
            max_slippage_percentage="0.03000000",
            auction_mode=False,
            high_bid_limit_percentage=""
        )
