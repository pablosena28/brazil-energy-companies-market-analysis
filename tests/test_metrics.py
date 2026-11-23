import pandas as pd
from src.data_cleaning import prepare_data
from src.metrics import annualized_volatility, max_drawdown, normalized_prices, period_return

def test_prepare_data_removes_exact_duplicates():
    df = pd.DataFrame({"Data":["2022-01-01","2022-01-02","2022-01-02"],"Empresa":[10.0,11.0,11.0]})
    assert len(prepare_data(df)) == 2

def test_period_return():
    assert round(period_return(pd.Series([100.0,110.0])),4) == 0.10

def test_max_drawdown():
    assert round(max_drawdown(pd.Series([100.0,120.0,90.0,110.0])),4) == -0.25

def test_annualized_volatility_is_non_negative():
    assert annualized_volatility(pd.Series([0.01,-0.02,0.015,-0.005])) >= 0

def test_normalized_prices_start_at_100():
    p = pd.DataFrame({"A":[20.0,22.0],"B":[10.0,9.0]})
    assert normalized_prices(p).iloc[0].tolist() == [100.0,100.0]
