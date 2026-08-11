import pandas as pd

df = pd.read_excel("employees.xlsx", sheet_name="Employee Details")

print("Data read from Excel file:")
print(df)