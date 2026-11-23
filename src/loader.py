from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

def load_prices() -> pd.DataFrame:
    files = sorted(RAW.glob("energy_companies_prices_part*.csv"))
    if not files:
        raise FileNotFoundError("Arquivos de dados não encontrados.")
    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    df["Data"] = pd.to_datetime(df["Data"])
    return df.sort_values("Data").drop_duplicates().reset_index(drop=True)
