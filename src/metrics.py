import numpy as np
import pandas as pd

def daily_returns(prices: pd.DataFrame) -> pd.DataFrame:
    return prices.pct_change()

def normalized_prices(prices: pd.DataFrame, base: float = 100.0) -> pd.DataFrame:
    return prices.div(prices.iloc[0]).mul(base)

def annualized_volatility(returns: pd.Series, periods: int = 252) -> float:
    return float(returns.dropna().std() * np.sqrt(periods))

def max_drawdown(prices: pd.Series) -> float:
    peak = prices.cummax()
    return float((prices / peak - 1).min())

def period_return(prices: pd.Series) -> float:
    return float(prices.iloc[-1] / prices.iloc[0] - 1)
