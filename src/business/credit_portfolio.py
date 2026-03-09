import pandas as pd

COLUMN_MAP = {
    "Exposure at Default": "ead",
    "Probability of Default": "pd",
    "Loss Given Default": "lgd"
}

REQUIRED_COLUMNS_RAW = [
    "loan_id",
    "segment",
    "Exposure at Default",
    "Probability of Default",
    "Loss Given Default",
    "interest_margin"
]

REQUIRED_COLUMNS_INTERNAL = [
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

    missing_raw = [col for col in REQUIRED_COLUMNS_RAW if col not in df.columns]
    if missing_raw:
        raise ValueError(f"Missing raw input columns: {missing_raw}")

    df = df.rename(columns=COLUMN_MAP)

    missing_internal = [col for col in REQUIRED_COLUMNS_INTERNAL if col not in df.columns]
    if missing_internal:
        raise ValueError(f"Missing internal columns after rename: {missing_internal}")

    return df
