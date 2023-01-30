# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# Add description here
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %%
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = None

# This is a placeholder, leave it as None
product = None


# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests

# %%
# NBA season we will be analyzing
year = 2022
# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/leagues/NBA_2022_per_game.html".format(year)
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html)

# %%
# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# exclude the first column because we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]
headers
# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

# %%
stats_22 = pd.DataFrame(stats_22, columns=["Player Name", "Position","Age","Team","G","GS","MP","FG","FGA","FGP","threeP","threePA","threePP","twoP","twoPA","twoPP","eFGP","FT","FTA","FTP","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS"])
#Printing to CSV
stats_22.to_csv("player_stats_22.csv", index=False)
print("Data saved to player_stats_22.csv")
stats.head(20)

# %%
stats_22.to_csv(product['data'], index=False)

# %%
#Season of 1956
# NBA season we will be analyzing
year = 1956
# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/leagues/NBA_1956_per_game.html".format(year)
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html)

# %%
# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# exclude the first column because we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]
headers
# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats_56 = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

# %%
stats_56 = pd.DataFrame(player_stats_56, columns=["Player Name", "Position","Age","Team","G","GS","MP","FG","FGA","FGP","threeP","threePA","threePP","twoP","twoPA","twoPP","eFGP","FT","FTA","FTP","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS"])
#Printing to CSV
stats_56.to_csv("player_stats_56.csv", index=False)
print("Data saved to player_stats_56.csv")
stats_56.head(20)

# %%
#Season of 1979
# NBA season we will be analyzing
year = 1979
# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/leagues/NBA_1980_per_game.html".format(year)
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html)

# %%
# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# exclude the first column because we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]
headers
# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats_79 = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

# %%
stats_79 = pd.DataFrame(player_stats_79, columns=["Player Name", "Position","Age","Team","G","GS","MP","FG","FGA","FGP","threeP","threePA","threePP","twoP","twoPA","twoPP","eFGP","FT","FTA","FTP","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS"])
#Printing to CSV
stats_79.to_csv("player_stats_79.csv", index=False)
print("Data saved to player_stats_79.csv")
stats_79.head(20)

# %%

# %%
#Season of 1995
# NBA season we will be analyzing
year = 1995
# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/leagues/NBA_1995_per_game.html".format(year)
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html)

# %%
# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# exclude the first column because we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]
headers
# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats_95 = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

# %%
stats_95 = pd.DataFrame(player_stats_95, columns=["Player Name", "Position","Age","Team","G","GS","MP","FG","FGA","FGP","threeP","threePA","threePP","twoP","twoPA","twoPP","eFGP","FT","FTA","FTP","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS"])
#Printing to CSV
stats_95.to_csv("player_stats_95.csv", index=False)
print("Data saved to player_stats_95.csv")
stats_95.head(20)

# %%
#Play by play nba stats

season_id = '2022-23'
per_mode = 'Totals'
player_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode='+per_mode+'&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season='+season_id+'-23&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# %%
headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# %%
requests.get(url=player_info_url, headers=headers).json()

# %%
player_info = response['resultsSet'][0]['rowSet']

# %%
