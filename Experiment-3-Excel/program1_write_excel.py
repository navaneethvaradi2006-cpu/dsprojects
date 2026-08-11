import pandas as pd

employee_data = {
    "Emp_ID": [201, 202, 203, 204],
    "Name": ["Rahul", "Sneha", "Arjun", "Priya"],
    "Department": ["IT", "HR", "Finance", "Marketing"],
    "Salary": [45000, 38000, 52000, 41000]
}

df = pd.DataFrame(employee_data)

df.to_excel("employees.xlsx", sheet_name="Employee Details", index=False)

print("Data successfully written to employees.xlsx")