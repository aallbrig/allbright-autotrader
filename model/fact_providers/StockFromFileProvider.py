from model.Stock import Stock


class StockFromFileProvider:
    def parse_args(self, argv: list[str]):
        raise NotImplementedError("Please Implement this method")

    def get_stocks(self) -> list[Stock]:
        raise NotImplementedError("Please Implement this method")
