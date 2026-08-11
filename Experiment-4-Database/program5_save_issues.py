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

df.to_csv("github_issues.csv", index=False)

print("GitHub Issues saved successfully.")
print("\nFirst five issues:")
print(df.head())