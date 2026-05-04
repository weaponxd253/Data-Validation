import re
import pandas as pd

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def _error(row, column, error, value=None):
    """Return a consistently shaped error dict."""
    return {"row": row, "column": column, "value": value, "error": error}


def validate_data(df: pd.DataFrame) -> list[dict]:
    errors = []

    required_columns = [
        "EmployeeID",
        "FirstName",
        "LastName",
        "Email",
        "HoursWorked",
        "Department",
    ]

    for column in required_columns:
        if column not in df.columns:
            errors.append(_error(None, column, "Missing required column"))

    if errors:
        return errors

    for index, row in df.iterrows():
        row_number = index + 2  # +2 because Excel rows are 1-indexed with a header

        if pd.isna(row["EmployeeID"]):
            errors.append(_error(row_number, "EmployeeID", "EmployeeID is blank"))

        if pd.isna(row["Department"]):
            errors.append(_error(row_number, "Department", "Department is blank"))

        if pd.notna(row["Email"]) and not EMAIL_REGEX.fullmatch(str(row["Email"]).strip()):
            errors.append(_error(row_number, "Email", "Invalid email format", row["Email"]))

        if pd.notna(row["HoursWorked"]) and row["HoursWorked"] < 0:
            errors.append(_error(row_number, "HoursWorked", "HoursWorked cannot be negative", row["HoursWorked"]))

    duplicate_ids = df[df["EmployeeID"].duplicated(keep=False)]

    for index, row in duplicate_ids.iterrows():
        errors.append(_error(index + 2, "EmployeeID", "Duplicate EmployeeID", row["EmployeeID"]))

    return errors