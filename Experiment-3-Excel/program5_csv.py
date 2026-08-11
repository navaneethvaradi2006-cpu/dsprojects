import pandas as pd

csv_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

csv_df = pd.read_csv(csv_url)

print("CSV Data:")
print(csv_df.head())

csv_df.to_csv("tips_data.csv", index=False)

print("\nCSV file written successfully.")