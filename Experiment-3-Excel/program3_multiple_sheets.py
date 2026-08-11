import pandas as pd

employee_data = {
    "Emp_ID": [201, 202, 203, 204],
    "Name": ["Rahul", "Sneha", "Arjun", "Priya"],
    "Department": ["IT", "HR", "Finance", "Marketing"],
    "Salary": [45000, 38000, 52000, 41000]
}

project_data = {
    "Project_ID": ["P101", "P102", "P103"],
    "Project_Name": ["Website", "Payroll", "Analytics"],
    "Duration": [6, 4, 8]
}

employees_df = pd.DataFrame(employee_data)
projects_df = pd.DataFrame(project_data)

with pd.ExcelWriter("company_data.xlsx", engine="openpyxl") as writer:
    employees_df.to_excel(writer, sheet_name="Employees", index=False)
    projects_df.to_excel(writer, sheet_name="Projects", index=False)

print("Multiple sheets successfully written to company_data.xlsx")