import pandas as pd
from validator.validate import validate_data

def test_missing_employee_id():
    df = pd.DataFrame({
        "EmployeeID": [None],
        "FirstName" : "Tony",
        "LastName": ["Stark"],
        "Email": ["ironman@stark.com"],
        "HoursWorked": [40],
        "Department": ["IT"]
    })

    errors = validate_data(df)

    assert any(e["column"] == "EmplyeeId" for e in errors)