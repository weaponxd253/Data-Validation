import pandas as pd
from collections import Counter


def export_results(df: pd.DataFrame, errors: list[dict]) -> None:
    has_column_errors = any(e["row"] is None for e in errors)

    if not has_column_errors:
        df.to_excel("data/output/cleaned_data.xlsx", index=False)
    else:
        print("Skipping cleaned_data.xlsx export — missing required columns must be fixed first.")

    error_df = pd.DataFrame(errors)

    if not error_df.empty:
        error_counts = Counter([e["error"] for e in errors])

        summary_df = pd.DataFrame({
            "Error Type": list(error_counts.keys()),
            "Count": list(error_counts.values())
        })

        with pd.ExcelWriter("data/output/error_report.xlsx", engine="openpyxl") as writer:
            error_df.to_excel(writer, index=False, sheet_name="Errors")
            summary_df.to_excel(writer, index=False, sheet_name="Summary")
    else:
        print("No validation errors found.")