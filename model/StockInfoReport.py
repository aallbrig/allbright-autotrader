from model.Stock import Stock


class StockInfoReport:
    stock: Stock

    def __init__(self, stock: Stock):
        self.stock = stock

    def __str__(self):
        return self._console_view()

    def _console_view(self):
        return f'Stock: {self.stock.symbol()}'
