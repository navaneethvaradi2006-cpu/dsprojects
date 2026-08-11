import sqlite3
import pandas as pd

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    name TEXT,
    department TEXT
)
""")

cursor.execute("INSERT INTO employees VALUES (1, 'Rahul', 'IT')")
cursor.execute("INSERT INTO employees VALUES (2, 'Sneha', 'HR')")

conn.commit()

df = pd.read_sql_query("SELECT * FROM employees", conn)

print("Employee Data:")
print(df)

cursor.execute("UPDATE employees SET name = 'Arjun' WHERE id = 1")
conn.commit()

cursor.execute("DELETE FROM employees WHERE id = 2")
conn.commit()

conn.close()

print("\nUpdate and Delete operations completed successfully.")