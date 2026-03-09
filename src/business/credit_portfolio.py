import pandas as pd

REQUIRED_COLUMNS = ["loan_id", "segment", "ead", "pd", "lgd", "interest_margin"]


def load_credit_portfolio(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df
