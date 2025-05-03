import src.doomscroller as scraper
import csv
# open counter.txt and read the number of sessions
with open("../output/sessions/counter.txt", "r") as f:
    session_counter = int(f.read())
print("Session #" + str(session_counter))

with open('../input/db/users.csv', newline='') as f:
    reader = csv.DictReader(f)
    creds = [(row['username'], row['password']) for row in reader]

username, password = creds[0] # modify this to get a specific user scraper. (the number represents Row Number)
print(f"Logging in {username} with password {password!r}")

scraper.scrape(username, password,
               session_counter,
               0.3,
               0,
               "",
               0,
               0,
               1,
               0,
               "",
               0,
               2,1, 0)

# increment the session counter
session_counter += 1
# write the new session counter to counter.txt
with open("../output/sessions/counter.txt", "w") as f:
    f.write(str(session_counter))


