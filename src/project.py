"""
project.py

Primary interface for the Fiverr Consulting Toolkit.

This class coordinates loading data, running quality checks,
performing analysis, and generating recommendations.
"""

from pathlib import Path

from src.io import (
    load_raw_data,
    save_master_dataset,
)

from src.etl import (
    build_master_dataset,
)

from src.quality import (
    dataset_report,
)

from src.analysis import (
    dataset_summary,
    search,
    keyword_frequency,
    price_summary,
    delivery_summary,
)


class FiverrToolkit:
    """
    Main interface for the Fiverr Consulting Toolkit.
    """

    def __init__(self):

        # Core data
        self.df = None

        # Future analysis objects
        self.summary = {}
        self.recommendations = []
        self.portfolio_projects = []

        # Project paths
        self.project_root = Path(__file__).resolve().parent.parent
        self.data_dir = self.project_root / "data"
        self.output_dir = self.data_dir / "processed"

    def __repr__(self):
        rows = len(self.df) if self.df is not None else 0
        return f"FiverrToolkit(rows={rows})"

    # --------------------------------------------------
    # Data
    # --------------------------------------------------

    def load(self):
        """
        Load and merge the raw Fiverr research datasets.
        """

        self.df = build_master_dataset()

        print(f"Loaded {len(self.df):,} rows.")

        return self.df

    def save(self):
        """
        Save the processed master dataset.
        """

        if self.df is None:
            raise ValueError("No dataframe has been loaded.")

        save_master_dataset(self.df)

        print("Master dataset saved.")

    # --------------------------------------------------
    # Reports
    # --------------------------------------------------

    def report(self):
        """
        Display a quality report.
        """

        if self.df is None:
            raise ValueError("No dataframe has been loaded.")

        dataset_report(self.df)

    # --------------------------------------------------
    # Convenience
    # --------------------------------------------------

    def head(self, rows=5):

        if self.df is None:
            raise ValueError("No dataframe has been loaded.")

        return self.df.head(rows)

    def columns(self):
        if self.df is None:
            raise ValueError("No dataframe has been loaded.")

        return list(self.df.columns)

    def shape(self):
        if self.df is None:
            raise ValueError("No dataframe has been loaded.")

        return self.df.shape

    # --------------------------------------------------
    # Analysis Functions
    # --------------------------------------------------
    def dataset_summary(self):
        return dataset_summary(self.df)

    def search(self, text):
        return search(self.df, text)

    def keyword_frequency(self):
        return keyword_frequency(self.df)

    def price_summary(self):
        return price_summary(self.df)

    def delivery_summary(self):
        return delivery_summary(self.df)
