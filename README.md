# Data Validation Engine

A Python tool that ingests employee data from Excel or CSV files, runs a suite of data quality checks, and produces structured Excel reports — clean enough to feed into downstream systems or AI pipelines.

Built to demonstrate Python fundamentals, pandas, automated reporting, and data quality engineering practices.

---

## Why This Exists

Real-world data is messy. Before employee data can be used in any meaningful way — analytics, payroll systems, or AI models — it needs to be validated and cleaned. This tool automates that process: it reads a file, flags every issue with its exact row and column, and exports a structured error report so problems can be fixed at the source.

---

## Features

- Accepts `.xlsx` or `.csv` input via command line
- Validates that all required columns are present
- Detects blank required fields (`EmployeeID`, `Department`)
- Flags invalid email formats using regex
- Catches negative hours worked
- Identifies duplicate Employee IDs
- Exports a two-sheet Excel error report (detail + summary)
- Skips the cleaned data export if the file has structural issues (missing columns)
- Consistent error schema across all validation rules
- Full unit test coverage with `pytest`

---

## Project Structure

```
DataValidation/
│
├── data/
│   ├── input/
│   │   └── employees.xlsx        # Sample input file
│   └── output/
│       ├── cleaned_data.xlsx     # Exported if no structural errors
│       └── error_report.xlsx     # Errors sheet + Summary sheet
│
├── src/
│   └── validator/
│       ├── __init__.py
│       ├── main.py               # Entry point
│       ├── load_data.py          # File loading
│       ├── validate.py           # All validation logic
│       └── export.py             # Excel report generation
│
├── tests/
│   └── test_validate.py          # pytest unit tests
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/data-validation-engine.git
cd data-validation-engine
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the validator

```bash
# Use the default input file
python src/validator/main.py

# Or pass any .xlsx or .csv file
python src/validator/main.py path/to/your_file.csv
```

---

## Input Format

Your file must contain these columns (additional columns are ignored):

| Column | Required | Validation |
|---|---|---|
| `EmployeeID` | Yes | Cannot be blank, no duplicates |
| `FirstName` | Yes | Must be present |
| `LastName` | Yes | Must be present |
| `Email` | No | Must match `user@domain.tld` if provided |
| `HoursWorked` | No | Cannot be negative if provided |
| `Department` | Yes | Cannot be blank |

---

## Output

Two files are written to `data/output/`:

**`error_report.xlsx`** — two sheets:
- `Errors`: every issue found, with its row number, column, the offending value, and a description
- `Summary`: a count of each error type across the whole file

**`cleaned_data.xlsx`** — the original data exported as-is. Only written if no structural errors (missing columns) were found.

---

## Running the Tests

```bash
pytest
```

Tests cover: happy path, missing columns, blank required fields, invalid and valid email formats, negative hours, duplicate IDs, and consistent error dict schema across all validation types.

---

## Tech Stack

- Python 3.12
- pandas
- openpyxl
- pytest

---

## Potential Extensions

- AI-generated plain-English summaries of the error report
- Auto-suggested fixes for common issues (e.g. inconsistent department names)
- Natural language validation rules ("flag anyone over 60 hours")
- Web interface for non-technical users to upload and review files
