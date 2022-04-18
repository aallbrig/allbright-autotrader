from models.fact_providers.ThirdPartyStockInfoProvider import ThirdPartyStockInfoProvider


class FinancialFactProvider:
    _providers: list[ThirdPartyStockInfoProvider] = []

    def __init__(self, providers: list[ThirdPartyStockInfoProvider]):
        self._providers = providers

    def inform_about_stocks(self):
        results = []

        for provider in self._providers:
            results.append(provider.retrieve_stock_info())

        return results
