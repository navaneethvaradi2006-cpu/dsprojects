import sqlite3
import pandas as pd

conn = sqlite3.connect("employees.db")

query = "SELECT * FROM employees WHERE department = 'IT'"

df = pd.read_sql_query(query, conn)

print("Employees from IT Department:")
print(df)

conn.close()