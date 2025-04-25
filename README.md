# COMP 396: Identifying Political Bias in the Instagram Reels Algorithm

## Scrapers

### 1. Simulated User Scraper
Activate it by running `mainsim.py`. 
All our credentials for created accounts for webscraping are in `input/db/users.csv` 
and are **accessed by row number** in `mainsim.py`.
Run 
`cd \Users\Admin\Programs\PycharmProjects\comp396` (wherever your project root is)
to get to your project's root
Then run:
`C:\Users\Admin\Programs\PycharmProjects\comp396\.venv\Scripts\python.exe -m src.maincol.py`
You modify the scraper settings in the inputs of the scraper function in `mainsim.py`.

```
scrape(
username, password,    # dont touch at all, credentials in creds[], change row number only
session,               # dont touch at all, session number from counter.txt file
watch_time_percentage, # touchable! % of reel duration spent watching
liked,                 # touchable! choose whether to like the reel or not
pos_comment_left,      # touchable! choose whether to leave a positive comment or not
                       ## put "" for no comment
                       ## write your comment as a string to comment it e.g. "Great video!" 
                       ## WARNING Instagram will ban you instantly.    
followed,              # touchable! choose whether to follow or not
shared,                # touchable! choose whether to share the reel or not
saved,                 # touchable! choose whether to save the reel or not
profile_visited,       # touchable! choose whether to visit the profile or not
neg_comment_left,      # touchable! choose whether to leave a negative comment or not
                       ## put "" for no comment
                       ## write your comment as a string to comment it e.g. "Bad video!" 
                       ## WARNING Instagram will ban you instantly.
clicked_not_interested,# 
quit_after, 
condition, 
political_bias):
```

### 2. Political Account Collector


