from src.model.StockInfoReport import StockInfoReport
from src.model.fact_providers.ThirdPartyStockInfoProvider import ThirdPartyStockInfoProvider


class TestThirdPartyStockInfoProvider(ThirdPartyStockInfoProvider):
    stock_info_reports: list[StockInfoReport]

    def retrieve_stock_info(self) -> list[StockInfoReport]:
        return self.stock_info_reports

    def __init__(self, stock_info_reports: list[StockInfoReport]):
        super().__init__([])
        self.stock_info_reports = stock_info_reports
