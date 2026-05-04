import argparse

from load_data import load_file
from validate import validate_data
from export import export_results


def parse_args():
    parser = argparse.ArgumentParser(description="Validate employee data from an Excel or CSV file.")
    parser.add_argument(
        "file_path",
        nargs="?",
        default="data/input/employees.xlsx",
        help="Path to input .xlsx or .csv file (default: data/input/employees.xlsx)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    df = load_file(args.file_path)
    errors = validate_data(df)
    export_results(df, errors)

    print(f"Validation complete. Errors found: {len(errors)}")

    print("----SUMMARY----")
    print(f"Total Rows: {len(df)}")
    print(f"Total errors: {len(errors)}")


if __name__ == "__main__":
    main()