from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt


if __name__ == '__main__':
    cerebro = bt.cerebro()

    print('starting portfolio value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('final portfolio value: %.2f' % cerebro.broker.getvalue())

