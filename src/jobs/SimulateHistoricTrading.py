import backtrader as bt

from model.command_line.CommandLineCommand import CommandLineCommand


class SimulateHistoricTrading(CommandLineCommand):
    _strategy: bt.Strategy = None

    def __init__(self, strategy: bt.Strategy, data_source: bt.dataseries):
        self._strategy = strategy

    def Execute(self, context):
        cerebro = bt.Cerebro()
        cerebro.addstrategy(self._strategy)
        print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
        cerebro.run()
        print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
