def dataset_report(df):
    print("=" * 50)
    print("MASTER DATASET REPORT")
    print("=" * 50)

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    duplicates = int(df.duplicated().sum())
    pct = duplicates / len(df) * 100

    print(f"Duplicate rows: {duplicates} ({pct:.1f}%)")

    if duplicates == 0:
        print("No duplicate rows")

    print()

    print("Column Types")
    print("-" * 50)
    print(df.dtypes)

    print()

    print("Missing Values")
    print("-" * 50)

    missing = df.isna().sum()
    missing = missing[missing > 0].sort_values(ascending=False)

    if missing.empty:
        print("No missing values.")
    else:
        print(missing)

    print()
    print(f"Shape: {df.shape}")

    print("=" * 50)
def duplicate_report():
    print("WRITE FUNCTION!: quality.duplicate_report called")

def missing_report():
    print("WRITE FUNCTION!: quality.missing_report called")

def column_summary():
    print("WRITE FUNCTION!: quality.column_summary called")

def value_counts():
    print("WRITE FUNCTION!: quality.value_counts called")
