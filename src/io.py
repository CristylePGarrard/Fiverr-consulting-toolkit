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

    return {
        "manual": manual,
        "about_me": about_me,
        "about_gig": about_gig,
        "gig_title": gig_title,
    }

