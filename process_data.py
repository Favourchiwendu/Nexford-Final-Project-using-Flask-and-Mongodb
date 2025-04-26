# process_data.py

import csv
from pymongo import MongoClient
from user import User  # import your User class

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]
collection = db["user_data"]

# Fetch data
data = list(collection.find())

# Create User objects
users = []

for record in data:
    user = User(
        age=record.get("age"),
        gender=record.get("gender"),
        income=record.get("income"),
        expenses=record.get("expenses", {})
    )
    users.append(user)

# Save to CSV
with open("survey_users.csv", mode="w", newline="") as file:
    fieldnames = ["age", "gender", "income", "utilities", "entertainment", "school_fees", "shopping", "healthcare"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for user in users:
        writer.writerow(user.to_dict())

print("Users successfully saved to survey_users.csv")
