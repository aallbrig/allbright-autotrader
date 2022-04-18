from models.Stock import Stock


# TODO: Common interface/class should map disparate data sources (like yahoo finance) into a common expected data struct

class ThirdPartyStockInfoProvider:
    _stock_picks: list[Stock]

    def __init__(self, stock_picks=None):
        if stock_picks is None:
            stock_picks = []
        self.set_stock_picks(stock_picks)

    def set_stock_picks(self, stock_picks: list[Stock]):
        self._stock_picks = stock_picks

    def retrieve_stock_info(self):
        raise NotImplementedError("Please Implement this method")
