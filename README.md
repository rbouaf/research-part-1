# Identifying Political Bias in the Instagram Reels Algorithm
Research with @JulesLemee under the supervision of Joseph Vybihal completed as part of the COMP 396 at McGill University.
## Scrapers
Avoiding Instagram's anti-bot detection and anti-scraping measures is the big roadblock in this project.
As data became even more valuable thanks to the explosion of LLM, companies like Meta have put in place much stricter anti-scrpaing measures, making scraping an uphill battle.
### 1. Simulated User Scraper
Activate it by running `mainsim.py`. 
All our credentials for created accounts for webscraping are in `input/db/users.csv` 
and are **accessed by row number** in `mainsim.py`.

Run <br>
`cd \Users\Admin\Programs\PycharmProjects\comp396` (wherever your project root is)
<br> to get to your project's root

Then run:<br>
`C:\Users\Admin\Programs\PycharmProjects\comp396\.venv\Scripts\python.exe -m src.maincol.py`

You modify the scraper settings in the inputs of the scraper function in `mainsim.py`.
<br>`mainsim.py` uses `doomscroll.py`

This will open a browser window and start scraping reels: it will perform actions on the reels based on the parameters you set in `mainsim.py`'s `scrape()` call.
Watch out, most actions will get you flagged as a bot and either disable features (you wont be able to like or follow) or ban you outright (if you leave the same comment many times, it bans you instantly)


| Parameters               | Editable?            | Info                                                                                                                                                                                                                        |
|--------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `username`, `password`   | dont touch directly  | credentials in creds[], change row number only                                                                                                                                                                              |
| `session`                | dont touch at all    | session number from counter.txt file                                                                                                                                                                                        |
| `watch_time_percentage`  | touchable            | % of reel duration spent watching                                                                                                                                                                                           |
| `liked`                  | touchable            | choose whether to like the reel or not                                                                                                                                                                                      |
| `pos_comment_left`       | touchable            | choose whether to leave a positive comment or not <br> put "" for no comment <br> write your comment as a string to comment it e.g. "Great video!" <br> WARNING Instagram will ban you instantly.                           |
| `followed`               | touchable            | choose whether to follow or not                                                                                                                                                                                             |
| `shared`                 | touchable            | choose whether to share the reel or not                                                                                                                                                                                     |
| `saved`                  | touchable            | choose whether to save the reel or not                                                                                                                                                                                      |
| `profile_visited`        | touchable            | choose whether to visit the profile or not                                                                                                                                                                                  |
| `neg_comment_left`       | touchable            | choose whether to leave a negative comment or not <br> put "" for no comment <br> write your comment as a string to comment it e.g. "Bad video!" <br> WARNING Instagram will ban you instantly.                             |
| `clicked_not_interested` | touchable            | choose whether to click not interested or not                                                                                                                                                                               |
| `quit_after`             | touchable            | number of reels to scrape this session                                                                                                                                                                                      |
| `condition`              | touchable            | CONDITIONAL BEHAVIOR:  <br/> if parameter condition is 1, then do everything for every reel <br/> if parameter condition is 2, then only do everything if the uploader is in the dataset AND the political bias is the same |
| `political_bias`         | touchable            | if `'L'` then only do things if the uploader is in the dataset AND the political bias is left <br/>if `'R'` then only do things if the uploader is in the dataset AND the political bias is right <br/>if `''` whatever     |

### 2. Political Account Collector
Activate it by running `maincol.py`.
All our credentials for created accounts for webscraping are in `input/db/users.csv`, 
and are **accessed by row number** in `maincol.py`.

This is a database builder that collects political accounts. 
It opens the uploader's profile and screenshots it then saves it to an AWS S3 bucket to make it accessible via a URL. It passes that URL to Instagram's API to get the political bias of the account. 
That data is added to the database. 

This is so that when we run the simulated user scraper (`mainsim.py`), we can check if the uploader is in the database and what their political bias is.
This is how we would evaluate whether the algorithm is biased or not. 

We are limited only by anti-bot and anti-scraping measures. If you can get over this hurdle, you're golden.

