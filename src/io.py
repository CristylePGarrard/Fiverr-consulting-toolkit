from pathlib import Path

import pandas as pd

DATA_DIR = Path("data")
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

def load_raw_data():
    manual = pd.read_csv(RAW_DIR / "FiverrResearch - ManualData.csv")
    about_me = pd.read_csv(RAW_DIR / "FiverrResearch - AboutMe.csv")
    about_gig = pd.read_csv(RAW_DIR / "FiverrResearch - AboutTheGig.csv")
    gig_title = pd.read_csv(RAW_DIR / "FiverrResearch - GigTitle.csv")
    return manual, about_me, about_gig, gig_title


def save_master_dataset(df):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / "master_dataset.csv", index=False)
    df.to_parquet(PROCESSED_DIR / "master_dataset.parquet", index=False)
