from model.StockInfoReport import StockInfoReport
from model.fact_providers.StockInformationProvider import StockInformationProvider


class FinancialFactProvider:
    _fact_provider: StockInformationProvider

    def __init__(self, provider: StockInformationProvider):
        self._fact_provider = provider

    def inform_about_stocks(self) -> list[StockInfoReport]:
        return self._fact_provider.retrieve_stock_info()
