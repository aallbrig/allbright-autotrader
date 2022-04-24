from model.command_line.CommandLineCommand import CommandLineCommand
from model.fact_providers import StockInformationProvider
from model.fact_providers.StockFromFileProvider import StockFromFileProvider


class SyncStockFactsFromSource(CommandLineCommand):
    fact_provider: StockInformationProvider
    file_provider: StockFromFileProvider

    def __init__(self, fact_provider: StockInformationProvider, file_provider: StockFromFileProvider):
        self.fact_provider = fact_provider
        self.file_provider = file_provider

    def Execute(self, context):
        self.file_provider.parse_args(context.argv)
        if not self.file_provider.is_valid():
            return 1
        stocks = self.file_provider.get_stocks()
        valid_stocks = stocks
        # check if there is a greater than 0 length of valid target stock
        # if not, return status code 1
        # else if length(valid_target_stocks) is greater than 1, proceed with logic
        self.fact_provider.set_stock_picks(valid_stocks)
        results = self.fact_provider.retrieve_stock_info()

        [context.command_line.print(f'{stock_info_report}') for stock_info_report in results]

        return 0
