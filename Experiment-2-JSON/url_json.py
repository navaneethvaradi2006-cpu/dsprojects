import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"

df = pd.read_json(url)

print("First Five Records")
print(df.head())