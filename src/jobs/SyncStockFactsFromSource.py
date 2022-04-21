import getopt

from src.model.command_line.CommandLineCommand import CommandLineCommand
from src.model.FinancialFactProvider import FinancialFactProvider
from src.model.Stock import Stock
from src.model.fact_providers.ThirdPartyStockInfoProvider import ThirdPartyStockInfoProvider


class SyncStockFactsFromSource(CommandLineCommand):
    input_file = None
    fact_provider: ThirdPartyStockInfoProvider

    def __init__(self, fact_provider: ThirdPartyStockInfoProvider):
        self.fact_provider = fact_provider

    def Execute(self, context):
        argv = context.argv

        try:
            opts, args = getopt.getopt(argv, "i:", ["input-file="])
        except getopt.GetoptError:
            print('--input-file,-i <input_file_path>')
            return 2
        for opt, arg in opts:
            if opt == '-h':
                print('--input-file ./data/STOCKS.txt')
                return 0
            elif opt in ("-i", "--input-file"):
                self.input_file = arg

        if self.input_file is not None:
            with open(self.input_file) as f:
                target_stocks = [Stock(line.strip()) for line in f.readlines()]
                # filter target_stock by if it is valid or not
                valid_target_stock = target_stocks
                # check if there is a greater than 0 length of valid target stock
                # if not, return status code 1
                # else if length(valid_target_stocks) is greater than 1, proceed with logic
                self.fact_provider.set_stock_picks(valid_target_stock)

        fact_provider = FinancialFactProvider(self.fact_provider)
        results = fact_provider.inform_about_stocks()

        # output string representations to the console
        [context.command_line.print(f'{stock_info_report}') for stock_info_report in results]
        return 0
