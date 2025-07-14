import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["sistercheck"]
collection = db["inventory"]

# Load Excel
excel_file = "Resources Inventory Cost Sheet.xlsx"  # Make sure this file is in the same folder
df = pd.read_excel(excel_file, sheet_name="Resources Inventory Cost Sheet")
df = df.where(pd.notnull(df), None)

# Upload to MongoDB
records = df.to_dict(orient="records")
collection.insert_many(records)

print(f"✅ Inserted {len(records)} records into MongoDB!")
