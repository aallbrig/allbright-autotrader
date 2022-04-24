from model.Stock import Stock
from model.fact_providers.StockProvider import StockProvider


class StockFromFileProvider(StockProvider):
    def get_stocks(self) -> list[Stock]:
        raise NotImplementedError("Please Implement this method")

    def parse_args(self, argv: list[str]):
        raise NotImplementedError("Please Implement this method")

