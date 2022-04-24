from model.Stock import Stock


class StockProvider:
    def get_stocks(self) -> list[Stock]:
        raise NotImplementedError("Please Implement this method")
