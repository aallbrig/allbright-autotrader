from datetime import datetime
from typing import Any

import backtrader as bt


# Create a subclass of Strategy to define the indicators and logic

class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params: dict[str, Any] = dict(
        period_fast=2,
        period_medium=30,
        period_slow=90
    )

    def log(self, txt, dt=None):
        """ Logging function fot this strategy"""
        dt = dt or self.data.datetime[0]
        if isinstance(dt, float):
            dt = bt.num2date(dt)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        simple_moving_average_short = bt.ind.SMA(period=self.p.period_fast)
        simple_moving_average_medium = bt.ind.SMA(period=self.p.period_medium)
        simple_moving_average_long = bt.ind.SMA(period=self.p.period_slow)
        self.short_cross_medium = bt.ind.CrossOver(simple_moving_average_short, simple_moving_average_medium)
        self.medium_cross_long = bt.ind.CrossOver(simple_moving_average_medium, simple_moving_average_long)

    def next(self):
        if self.position:
            # if self.short_cross_medium < 0 and self.medium_cross_long < 0:
            if self.short_cross_medium < 0:
                self.log('SELL CREATE, %.2f' % self.data.close[0])
                self.sell()

        # elif self.short_cross_medium > 0 and self.medium_cross_long > 0:
        elif self.short_cross_medium > 0:
            self.log('BUY CREATE, %.2f' % self.data.close[0])
            self.buy()


if __name__ == "__main__":
    cerebro = bt.Cerebro()  # create a "Cerebro" engine instance

    # Create a data feed
    from_date = datetime(2000, 1, 1)
    to_date = datetime(2022, 4, 25)
    for ticker in ['MRNA', 'MSFT', 'PFE', 'SPY', 'TSLA', 'U', 'VNQ', 'VOO']:
        cerebro.adddata(
            bt.feeds.YahooFinanceData(
                dataname=f'./data/{ticker}.csv',
                fromdate=from_date,
                todate=to_date
            )
        )

    cerebro.addobserver(bt.observers.Broker)
    cerebro.addstrategy(SmaCross)

    start_value = cerebro.broker.getvalue()

    print('Starting Portfolio Value: %.2f' % start_value)
    cerebro.run()  # run it all
    end_value = cerebro.broker.getvalue()
    print('Ending Portfolio Value: %.2f' % end_value)
    change_value = end_value - start_value
    print('Portfolio Change: %.2f' % change_value)

    cerebro.plot(start=from_date, end=to_date)
