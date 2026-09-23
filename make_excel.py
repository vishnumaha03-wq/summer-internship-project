import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

print("Generating 10,000 rows of test data. Please wait a few seconds...")

num_rows = 10000
details = ['Cost of Sales', 'Credit Expenses', 'Credit Sales', 'Cash Sales', 'Inventory Purchase']

data = []
start_date = datetime(2022, 1, 1)

# 1. Create the base data
for i in range(num_rows):
    data.append({
        "EntryNo": float(i + 1),
        "Date": (start_date + timedelta(days=random.randint(0, 700))).strftime("%Y-%m-%d %H:%M:%S"),
        "Territory_key": random.choice([1, 2, 3]),
        "Account_key": random.choice([60, 230, 280, 100, 400]),
        "Details": random.choice(details),
        "Amount": random.randint(-5000, 15000),
        "Unnamed: 6": np.nan, "Unnamed: 7": np.nan, "Unnamed: 8": np.nan,
        "Unnamed: 9": np.nan, "Unnamed: 10": np.nan, "Unnamed: 11": np.nan
    })

df = pd.DataFrame(data)

# 2. Hide 50 "Missing Invoice" errors (remove EntryNo)
for idx in random.sample(range(num_rows), 50):
    df.at[idx, "EntryNo"] = np.nan

# 3. Hide 50 "Uncoded Transaction" errors (set Account_key to 0)
for idx in random.sample(range(num_rows), 50):
    df.at[idx, "Account_key"] = 0

# 4. Hide 20 "Duplicate Transaction" errors
duplicates = df.sample(20).copy()
df = pd.concat([df, duplicates], ignore_index=True)

# 5. Shuffle the data and save it as an Excel file
df = df.sample(frac=1).reset_index(drop=True)
df.to_excel("massive_glerrors.xlsx", index=False)

print("Success! 'massive_glerrors.xlsx' has been created in your folder.")