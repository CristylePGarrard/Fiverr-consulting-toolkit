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

def build_master_dataset():
    manual, about_me, about_gig, gig_title = load_raw_data()
    # Rename columns for clarity
    gig_title = gig_title.rename(columns={"ID": "gig_title_id", gig_title.columns[1]: "gig_title"})
    about_gig = about_gig.rename(columns={"ID": "about_gig_id", about_gig.columns[1]: "about_gig"})
    about_me = about_me.rename(columns={"ID": "about_me_id", about_me.columns[1]: "about_me"})
    # Rename FK columns in manual data
    manual = manual.rename(columns={"Gig Title": "gig_title_id", "About the Gig": "about_gig_id", "About Me": "about_me_id"})
    manual = manual.rename(columns={"Delivery Timeline (days)": "DeliveryTimeline"})
    # Merge
    master = (manual.merge(gig_title, on="gig_title_id", how="left").merge(about_gig, on="about_gig_id", how="left").merge(about_me, on="about_me_id", how="left"))
    return master

def save_master_dataset(df):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / "master_dataset.csv", index=False)
    df.to_parquet(PROCESSED_DIR / "master_dataset.parquet", index=False)

def dataset_report(df):
    print("=" * 50)
    print("MASTER DATASET REPORT")
    print("=" * 50)
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    if int(df.duplicated().sum()) > 0:
        print(f"Duplicate rows: {df.duplicated().sum()}")
    else:
        print("No duplicate rows")
    print("Column Types")
    print("-" * 50)
    print(df.dtypes)
    missing = df.isna().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    if len(missing) > 0:
        print("Columns Missing Values:")
        print(missing.head(20))
    else:
        print("No missing values detected.")
        print("=" * 50)
