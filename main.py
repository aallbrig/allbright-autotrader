#!/usr/bin/python
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

from src.model.command_line.CommandLine import CommandLine
from src.model.command_line.CommandLineApp import CommandLineApp
from src.fact_providers.YahooFinanceStockInfoProvider import YahooFinanceStockInfoProvider
from src.jobs.SyncStockFactsFromSource import SyncStockFactsFromSource
from src.jobs.ExecuteTrading import ExecuteTrading
from src.jobs.SimulateHistoricTrading import SimulateHistoricTrading
from src.model.command_line.CommandRegistry import CommandRegistry


def build_fact_producer_command():
    yahoo_finance_provider = YahooFinanceStockInfoProvider()
    return SyncStockFactsFromSource(yahoo_finance_provider)


def build_simulator_command():
    return SimulateHistoricTrading()


def build_trader_command():
    return ExecuteTrading()


def build_command_registry() -> CommandRegistry:
    command_registry = CommandRegistry()

    command_registry.set('job-sync-facts', build_fact_producer_command)
    command_registry.set('job-simulate-historic-trading', build_simulator_command)
    command_registry.set('job-execute-trading-strategy', build_trader_command)

    return command_registry


class CommandLine(CommandLine):

    def print(self, message: str):
        print(message)


def main(argv):
    app = CommandLineApp(CommandLine(), build_command_registry())
    exit_code = app.run(argv)
    sys.exit(exit_code)


if __name__ == '__main__':
    main(sys.argv[1:])
