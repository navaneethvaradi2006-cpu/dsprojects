import pandas as pd

excel_data = pd.read_excel(
    "company_data.xlsx",
    sheet_name=None
)

print("Available Sheets:")
print(excel_data.keys())

print("\nEmployee Sheet:")
print(excel_data["Employees"])

print("\nProject Sheet:")
print(excel_data["Projects"])