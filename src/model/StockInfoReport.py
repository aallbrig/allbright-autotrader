from src.model.Stock import Stock


class StockInfoReport:
    stock: Stock

    def __init__(self, stock: Stock):
        self.stock = stock
