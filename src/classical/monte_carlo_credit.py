import numpy as np
import pandas as pd


def run_credit_monte_carlo(df: pd.DataFrame, n_sims: int = 5000, seed: int = 42):
    rng = np.random.default_rng(seed)
    losses = []

    for _ in range(n_sims):
        defaults = rng.random(len(df)) < df["pd"].values
        loss = np.sum(defaults * df["ead"].values * df["lgd"].values)
        losses.append(loss)

    losses = np.array(losses)

    return {
        "expected_loss": float(np.mean(losses)),
        "std_loss": float(np.std(losses)),
        "var_95": float(np.percentile(losses, 95)),
        "losses": losses,
    }
