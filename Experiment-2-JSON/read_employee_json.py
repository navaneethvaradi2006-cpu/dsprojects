import pandas as pd

# Read JSON file
df = pd.read_json("employees.json")

print("===== Employee Data =====")
print(df)

print("\n===== First Five Rows =====")
print(df.head())

print("\n===== Dataset Information =====")
df.info()

print("\n===== Shape =====")
print(df.shape)

print("\n===== Column Names =====")
print(df.columns)