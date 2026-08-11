import sqlite3
import pandas as pd

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

print("===== Before Update =====")

df = pd.read_sql_query("SELECT * FROM employees", conn)
print(df)

cursor.execute(
    "UPDATE employees SET name = 'Arjun' WHERE id = 1"
)
conn.commit()

print("\n===== After Update =====")

df = pd.read_sql_query("SELECT * FROM employees", conn)
print(df)

cursor.execute(
    "DELETE FROM employees WHERE id = 2"
)
conn.commit()

print("\n===== After Delete =====")

df = pd.read_sql_query("SELECT * FROM employees", conn)
print(df)

conn.close()

print("\nUpdate and Delete completed successfully.")