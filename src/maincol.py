import src.collector as scraper
import csv
import os
path_to_users = os.path.join("input", "db", "users.csv")
with open(path_to_users, newline='') as f:
    reader = csv.DictReader(f)
    creds = [(row['username'], row['password']) for row in reader]

username, password = creds[3]
print(f"Logging in {username} with password {password!r}")

scraper.scrape(username, password, 9999999999999)


