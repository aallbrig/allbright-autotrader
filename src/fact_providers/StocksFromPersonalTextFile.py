import getopt

from model.Stock import Stock
from model.fact_providers.StockFromFileProvider import StockFromFileProvider


def _parse_line_strategy(line):
    return line.strip()


class StocksFromPersonalTextFile(StockFromFileProvider):
    input_file = None

    def parse_args(self, argv: list[str]):
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

    def get_stocks(self) -> list[Stock]:
        if self.is_valid():
            with open(self.input_file) as f:
                stocks = [Stock(_parse_line_strategy(line)) for line in f.readlines()]
                return stocks
        else:
            return []

    def is_valid(self):
        return self.input_file is not None

