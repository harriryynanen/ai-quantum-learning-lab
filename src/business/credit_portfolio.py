import pandas as pd

COLUMN_MAP = {
    "Exposure at Default": "ead",
    "Probability of Default": "pd",
    "Loss Given Default": "lgd"
}

REQUIRED_COLUMNS = [
    "loan_id",
    "segment",
    "ead",
    "pd",
    "lgd",
    "interest_margin"
]

def load_credit_portfolio(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    df = df.rename(columns=COLUMN_MAP)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df
