import requests
import pandas as pd

url = "https://api.github.com/repos/python/cpython/issues"

response = requests.get(url)

issues = response.json()

data = []

for issue in issues:
    data.append({
        "id": issue["id"],
        "title": issue["title"],
        "state": issue["state"],
        "user": issue["user"]["login"]
    })

df = pd.DataFrame(data)

print("GitHub Issues Data:")
print(df.head())

print("\nNumber of Issues:")
print(len(df))