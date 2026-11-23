import pandas as pd
from src.loader import load_prices
from src.data_cleaning import prepare_data
from src.metrics import annualized_volatility, daily_returns, max_drawdown, period_return

def main() -> None:
    df = prepare_data(load_prices())
    companies = [c for c in df.columns if c != "Data"]
    prices = df.set_index("Data")[companies]
    returns = daily_returns(prices)

    rows = []
    for company in companies:
        rows.append({
            "Empresa": company,
            "Retorno (%)": period_return(prices[company]) * 100,
            "Volatilidade (%)": annualized_volatility(returns[company]) * 100,
            "Drawdown máximo (%)": max_drawdown(prices[company]) * 100,
        })

    result = pd.DataFrame(rows).sort_values("Retorno (%)", ascending=False)
    print("=== EMPRESAS DE ENERGIA ===")
    print(f"Observações únicas: {len(df)}")
    print(f"Período: {df['Data'].min().date()} a {df['Data'].max().date()}")
    print("\n=== RISCO E RETORNO ===")
    print(result.round(2).to_string(index=False))
    print("\n=== CORRELAÇÃO DOS RETORNOS ===")
    print(returns.corr().round(2).to_string())

if __name__ == "__main__":
    main()
