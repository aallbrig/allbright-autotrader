class StockNowSummary:
    current: float = 0.0

    def __str__(self):
        return f'Current Price: {self.current}'
