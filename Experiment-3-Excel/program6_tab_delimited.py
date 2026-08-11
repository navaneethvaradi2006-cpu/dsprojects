import pandas as pd

employee_data = {
    "Emp_ID": [201, 202, 203, 204],
    "Name": ["Rahul", "Sneha", "Arjun", "Priya"],
    "Department": ["IT", "HR", "Finance", "Marketing"],
    "Salary": [45000, 38000, 52000, 41000]
}

employee_df = pd.DataFrame(employee_data)

employee_df.to_csv(
    "employee_data.txt",
    sep="\t",
    index=False
)

tab_df = pd.read_csv(
    "employee_data.txt",
    sep="\t"
)

print("Tab-Delimited Data:")
print(tab_df)
