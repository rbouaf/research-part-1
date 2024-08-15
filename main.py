import lab_rat_scaper.scraper as scraper

# # open session_counter.txt and read the number of sessions
# with open("session_counter.txt", "r") as f:
#     session_counter = int(f.read())

scraper.scrape("minesweeper_enthusiast",
               "marco1231$",
               1,
               0.3,
               1,
               "",
               1,
               0,
               0,
               0,
               "",
               0,
               10,
               1)

# increment the session counter
# session_counter += 1