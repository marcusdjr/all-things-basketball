# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
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
stats_22 = pd.DataFrame(player_stats, columns=["Player Name", "Position","Age","Team","G","GS","MP","FG","FGA","FGP","threeP","threePA","threePP","twoP","twoPA","twoPP","eFGP","FT","FTA","FTP","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS"])
#Printing to CSV
stats.to_csv("player_stats_22.csv", index=False)
print("Data saved to player_stats.csv")
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
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

# %%
stats_56 = pd.DataFrame(player_stats, columns=["Player Name", "Position","Age","Team","G","GS","MP","FG","FGA","FGP","threeP","threePA","threePP","twoP","twoPA","twoPP","eFGP","FT","FTA","FTP","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS"])
#Printing to CSV
stats.to_csv("player_stats_56.csv", index=False)
print("Data saved to player_stats.csv")
stats_56.head(20)

# %%

# %%
