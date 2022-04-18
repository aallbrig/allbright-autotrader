import getopt
import sys

from models.command_line.CommandLineCommand import CommandLineCommand
from models.FinancialFactProvider import FinancialFactProvider
from models.Stock import Stock
from models.fact_providers.ThirdPartyStockInfoProvider import ThirdPartyStockInfoProvider


class SyncStockFactsFromSource(CommandLineCommand):
    input_file = None
    fact_providers: list[ThirdPartyStockInfoProvider] = []

    def __init__(self, fact_providers):
        self.fact_providers = fact_providers

    def Execute(self, context):
        argv = context.argv

        try:
            opts, args = getopt.getopt(argv[1:], "i:", ["input-file="])
        except getopt.GetoptError:
            print('--input-file,-i <input_file_path>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('main.py --input-file ./data/STOCKS.txt')
                sys.exit()
            elif opt in ("-i", "--input-file"):
                self.input_file = arg

        if self.input_file is not None:
            with open(self.input_file) as f:
                target_stocks = [Stock(line.strip()) for line in f.readlines()]
                [provider.set_stock_picks(target_stocks) for provider in self.fact_providers]

        fact_provider = FinancialFactProvider(self.fact_providers)
        results = fact_provider.inform_about_stocks()
        print(results)
