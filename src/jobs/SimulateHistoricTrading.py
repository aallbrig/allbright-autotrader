import backtrader as bt

from src.model.command_line.CommandLineCommand import CommandLineCommand


class SimulateHistoricTrading(CommandLineCommand):
    def Execute(self, context):
        cerebro = bt.Cerebro()
        print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
        cerebro.run()
        print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
