import scraper_simulated_user.doomscroller as scraper

# open counter.txt and read the number of sessions
with open("../data_output/sessions/counter.txt", "r") as f:
    session_counter = int(f.read())
print("Session #" + str(session_counter))

scraper.scrape("michealjoneshenny","benis1234",
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
               10,1, 0)

# increment the session counter
session_counter += 1
# write the new session counter to counter.txt
with open("../data_output/sessions/counter.txt", "w") as f:
    f.write(str(session_counter))


