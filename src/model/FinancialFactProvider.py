from src.model.StockInfoReport import StockInfoReport
from src.model.fact_providers.ThirdPartyStockInfoProvider import ThirdPartyStockInfoProvider


class FinancialFactProvider:
    _fact_provider: ThirdPartyStockInfoProvider

    def __init__(self, provider: ThirdPartyStockInfoProvider):
        self._fact_provider = provider

    def inform_about_stocks(self) -> list[StockInfoReport]:
        return self._fact_provider.retrieve_stock_info()
