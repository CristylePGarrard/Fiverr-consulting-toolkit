"""
analysis.py

Analysis functions for the Fiverr Consulting Toolkit.

These functions perform exploratory data analysis (EDA) on the Fiverr
research dataset. They do not modify the original DataFrame.

Author: Cristyle P Garrard
Project: Fiverr Consulting Toolkit
"""

from collections import Counter

import pandas as pd


# ==========================================================
# Default columns searched by the search() function
# ==========================================================

SEARCH_COLUMNS = [
    "gig_title",
    "Caption",
    "Description",
    "about_gig",
    "about_me",
]


# ==========================================================
# Dataset Summary
# ==========================================================

def dataset_summary(df):
    summary = {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Missing Values": int(df.isna().sum().sum()),
    }

    return (
        pd.Series(summary, name="Dataset")
        .to_frame()
    )


# ==========================================================
# Search
# ==========================================================

def search(df, text, columns=None, case=False):
    """
    Search one or more text columns.

    Parameters
    ----------
    df : pandas.DataFrame

    text : str
        Text to search for.

    columns : list[str], optional
        Columns to search. If omitted, SEARCH_COLUMNS is used.

    case : bool
        Case-sensitive search.

    Returns
    -------
    pandas.DataFrame
    """

    if columns is None:
        columns = SEARCH_COLUMNS

    columns = [c for c in columns if c in df.columns]

    if not columns:
        raise ValueError("No searchable columns exist in DataFrame.")

    mask = pd.Series(False, index=df.index)

    for column in columns:
        mask |= (
            df[column]
            .fillna("")
            .astype(str)
            .str.contains(text, case=case, regex=False)
        )

    return df.loc[mask].copy()


# ==========================================================
# Numeric Summary
# ==========================================================

def numeric_summary(df):
    """
    Return descriptive statistics for numeric columns.
    """

    return df.describe().T


# ==========================================================
# Missing Values
# ==========================================================

def missing_values(df):
    """
    Return missing value counts.
    """

    missing = (
        df.isna()
        .sum()
        .sort_values(ascending=False)
    )

    return missing[missing > 0]


# ==========================================================
# Top Values
# ==========================================================

def top_values(df, column, n=10):
    """
    Return the most common values for a column.
    """

    if column not in df.columns:
        raise ValueError(f"{column} not found.")

    return df[column].value_counts().head(n)


# ==========================================================
# Price Summary
# ==========================================================

def price_summary(df, column="Cost"):
    """
    Return pricing statistics.
    """

    if column not in df.columns:
        raise ValueError(f"{column} not found.")

    return df[column].describe()


# ==========================================================
# Delivery Summary
# ==========================================================

def delivery_summary(df):
    """
    Summarize delivery timelines.
    """

    if "DeliveryTimeline" not in df.columns:
        raise ValueError("DeliveryTimeline column not found.")

    return df["DeliveryTimeline"].describe()


# ==========================================================
# Keyword Frequency
# ==========================================================

def keyword_frequency(df, column="Description", top=25):
    """
    Count the most common words in a text column.

    This is intentionally simple for now.
    Later we'll replace it with proper NLP.
    """

    if column not in df.columns:
        raise ValueError(f"{column} not found.")

    words = []

    for text in df[column].fillna(""):
        words.extend(
            str(text)
            .lower()
            .replace(",", " ")
            .replace(".", " ")
            .split()
        )

    counts = Counter(words)

    return (
        pd.DataFrame(
            counts.items(),
            columns=["word", "count"]
        )
        .sort_values("count", ascending=False)
        .head(top)
        .reset_index(drop=True)
    )