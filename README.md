# Data Validation Engine

A Python-based data validation tool that reads employee data from an Excel or CSV file, checks for common data quality issues, and generates structured output reports.

This project was built to practice Python, pandas, data validation, automated reporting, and testing concepts.

---

## Features

- Reads data from `.xlsx` or `.csv` files
- Validates required columns
- Detects missing values
- Detects duplicate employee IDs
- Checks for invalid email formats
- Checks for negative hours worked
- Exports cleaned data
- Generates an Excel error report
- Creates a summary sheet showing error counts
- Includes unit testing with `pytest`

---

## Project Structure

```text
DataValidation/
│
├── data/
│   ├── input/
│   │   └── employees.xlsx
│   │
│   └── output/
│       ├── cleaned_data.xlsx
│       └── error_report.xlsx
│
├── src/
│   └── validator/
│       ├── __init__.py
│       ├── main.py
│       ├── load_data.py
│       ├── validate.py
│       └── export.py
│
├── tests/
│   └── test_validate.py
│
├── requirements.txt
├── pytest.ini
└── README.md
