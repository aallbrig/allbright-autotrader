#!/usr/bin/python
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

from src.model.command_line.CommandLineContext import CommandLineContext
from src.fact_providers.YahooFinanceStockInfoProvider import YahooFinanceStockInfoProvider
from src.jobs.SyncStockFactsFromSource import SyncStockFactsFromSource
from src.jobs.ExecuteTrading import ExecuteTrading
from src.jobs.SimulateHistoricTrading import SimulateHistoricTrading


def main(argv):
    possible_subcommand = argv[0]
    if possible_subcommand == 'job-sync-facts':
        yahoo_finance_provider = YahooFinanceStockInfoProvider()
        SyncStockFactsFromSource(yahoo_finance_provider).Execute(CommandLineContext(argv))
    elif possible_subcommand == 'job-simulate-historic-trading':
        SimulateHistoricTrading().Execute(CommandLineContext(argv))
    elif possible_subcommand == 'job-execute-trading-strategy':
        ExecuteTrading().Execute(CommandLineContext(argv))


if __name__ == '__main__':
    main(sys.argv[1:])
