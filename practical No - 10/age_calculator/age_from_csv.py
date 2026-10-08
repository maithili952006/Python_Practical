import pandas as pd
from datetime import date

# Read CSV file
df = pd.read_csv("student.csv")

# Convert Birthdate into date format
df["Birthdate"] = pd.to_datetime(df["Birthdate"])

# Get current system date
today = date.today()

# Calculate age in years
df["Age_Years"] = today.year - df["Birthdate"].dt.year

# Calculate age in months
df["Age_Months"] = today.month - df["Birthdate"].dt.month

# Check whether birthday has occurred this year
for i in range(len(df)):

    birth_date = df.loc[i, "Birthdate"]

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        df.loc[i, "Age_Years"] = df.loc[i, "Age_Years"] - 1
        df.loc[i, "Age_Months"] = df.loc[i, "Age_Months"] - 1

    if df.loc[i, "Age_Months"] < 0:
        df.loc[i, "Age_Months"] = df.loc[i, "Age_Months"] + 12

print("Current System Date:", today)

print("\nStudent Details:")
print(df)