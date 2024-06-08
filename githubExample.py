from backtesting import Backtest
from backtesting.test import GOOG
from backtesting import Strategy
from backtesting.lib import crossover
import pandas as pd

def SMA(values, n):
    """
    Return simple moving average of `values`, at
    each step taking into account `n` previous values.
    """
    return pd.Series(values).rolling(n).mean()

class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 20
    
    def init(self):
        # Precompute the two moving averages
        #data supposed to be GOOG(by me)
        #self.data.close=>pandas series of data(by me)
        self.sma1 = self.I(SMA, self.data.Close, self.n1)#self.smai=series of data(GOOG)(by me)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()
bt = Backtest(GOOG, SmaCross, cash=10_000, commission=.002)#SmaCross works with GOOG as a data(by me)-SmCross is like alogrithm(strategy)given to Backtest to plot it
stats = bt.run()
print(stats)
bt.plot()
