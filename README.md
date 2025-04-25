# COMP 396: Identifying Political Bias in the Instagram Reels Algorithm

## Scrapers

### 1. Simulated User Scraper
Activate it by running `mainsim.py`. 
All our credentials for created accounts for webscraping are in `input/db/users.csv` 
and are **accessed by row number** in `mainsim.py`.

You modify the scraper settings in the inputs of the scraper function in `mainsim.py`.
```
scrape(
username, password,    # dont touch at all, credentials in creds[], change row number only
session,               # dont touch at all, session number from counter.txt file
watch_time_percentage, # touchable! % of reel duration spent watching
liked,                 # touchable! choose whether to like the reel or not
pos_comment_left,      # touchable! choose whether to leave a positive comment or not
followed,               
shared, 
saved, 
profile_visited, 
neg_comment_left, 
clicked_not_interested,
quit_after, 
condition, 
political_bias):
```

### 2. Political Account Collector


