#!/usr/bin/python
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

from models.command_line.CommandLineContext import CommandLineContext
from src.fact_providers.YahooFinanceStockInfoProvider import YahooFinanceStockInfoProvider
from src.jobs.SyncStockFactsFromSource import SyncStockFactsFromSource
from src.jobs.ExecuteTrading import ExecuteTrading
from src.jobs.SimulateHistoricTrading import SimulateHistoricTrading


def main(argv):
    if argv[0] == 'job-sync-facts':
        yahoo_finance_provider = YahooFinanceStockInfoProvider()
        fact_providers = [yahoo_finance_provider]
        SyncStockFactsFromSource(fact_providers).Execute(CommandLineContext(argv))
    elif argv[0] == 'job-simulate-historic-trading':
        SimulateHistoricTrading().Execute(CommandLineContext(argv))
    elif argv[0] == 'job-execute-trading-strategy':
        ExecuteTrading().Execute(CommandLineContext(argv))


if __name__ == '__main__':
    main(sys.argv[1:])
