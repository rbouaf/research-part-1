import src.collector as scraper
import csv

with open('../input/db/users.csv', newline='') as f:
    reader = csv.DictReader(f)
    creds = [(row['username'], row['password']) for row in reader]

username, password = creds[0]
print(f"Logging in {username} with password {password!r}")

scraper.scrape(username, password, 3)


