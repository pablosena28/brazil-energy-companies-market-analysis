import pandas as pd

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    if "Data" not in df.columns:
        raise ValueError("Coluna 'Data' não encontrada.")
    data = df.copy()
    data["Data"] = pd.to_datetime(data["Data"], errors="raise")
    if data.isna().any().any():
        raise ValueError("A base contém valores ausentes.")
    data = data.drop_duplicates().sort_values("Data").reset_index(drop=True)
    if data["Data"].duplicated().any():
        raise ValueError("Há datas duplicadas com valores diferentes.")
    return data
