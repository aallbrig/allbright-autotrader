class StockDaySummary:
    # what is the format of 2010-06-29 ?
    date_format: str = "%Y-%m-%d"
    date: str
    open: float
    high: float
    low: float
    close: float
    # adjusted close definition
    # > Adjusted close is the closing price after adjustments for all applicable splits and dividend distributions
    # further reading: https://www.investopedia.com/terms/a/adjusted_closing_price.asp
    adjusted_close: float
    trade_volume: int
