from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from src.loader import load_prices
from src.data_cleaning import prepare_data
from src.metrics import daily_returns, normalized_prices

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "reports" / "figures"

def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    df = prepare_data(load_prices())
    companies = [c for c in df.columns if c != "Data"]
    prices = df.set_index("Data")[companies]
    returns = daily_returns(prices)
    normalized = normalized_prices(prices)

    fig, ax = plt.subplots(figsize=(12, 6))
    for c in companies:
        ax.plot(normalized.index, normalized[c], label=c)
    ax.axhline(100, linestyle="--", linewidth=1)
    ax.set_title("Desempenho relativo das empresas de energia")
    ax.set_ylabel("Índice base 100")
    ax.grid(True, alpha=0.25)
    ax.legend(ncol=3, frameon=False)
    fig.tight_layout()
    fig.savefig(FIGURES / "normalized_performance.svg", bbox_inches="tight")
    plt.close(fig)

    corr = returns.corr()
    fig, ax = plt.subplots(figsize=(8, 7))
    im = ax.imshow(corr.values, vmin=-1, vmax=1)
    ax.set_xticks(range(len(companies)))
    ax.set_yticks(range(len(companies)))
    ax.set_xticklabels(companies, rotation=35, ha="right")
    ax.set_yticklabels(companies)
    for i in range(len(companies)):
        for j in range(len(companies)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")
    ax.set_title("Correlação entre retornos diários")
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(FIGURES / "returns_correlation.svg", bbox_inches="tight")
    plt.close(fig)

if __name__ == "__main__":
    main()
