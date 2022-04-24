from model.Stock import Stock
from model.fact_providers.StockFromFileProvider import StockFromFileProvider


class FakeStockFromFileProvider(StockFromFileProvider):
    def is_valid(self):
        return True

    def get_stocks(self) -> list[Stock]:
        pass

    def parse_args(self, argv: list[str]):
        pass

