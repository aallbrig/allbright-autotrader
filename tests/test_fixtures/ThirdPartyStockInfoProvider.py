from src.model.Stock import Stock
from src.model.StockInfoReport import StockInfoReport
from src.model.fact_providers.StockInformationProvider import StockInformationProvider


class TestThirdPartyStockInfoProvider(StockInformationProvider):
    stock_info_reports: list[StockInfoReport]

    def retrieve_stock_info(self) -> list[StockInfoReport]:
        return self.stock_info_reports

    def __init__(self, stocks: list[Stock] = None, stock_info_reports: list[StockInfoReport] = None):
        if stock_info_reports is None:
            stock_info_reports = []
        if stocks is None:
            stocks = []
        super().__init__(stocks)
        self.stock_info_reports = stock_info_reports
