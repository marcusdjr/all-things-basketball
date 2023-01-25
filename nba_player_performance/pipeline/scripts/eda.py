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
upstream = ['clean']

# This is a placeholder, leave it as None
product = None


# %%
#Notes 
#Over the years, teams and analysts have started using advanced metrics to evaluate player performance. This has led to a deeper understanding of the game and has changed the way teams evaluate and build their rosters.

#The average number of points per game for NBA players has increased over time. This can be attributed to an increase in the pace of play, more efficient offenses, and a greater emphasis on three-point shooting.

# %%
import pandas as pd
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# # %matplotlib inline
import matplotlib.pyplot as plt  # Matlab-style plotting
import seaborn as sns
stats_22 = pd.read_csv(upstream['clean']['data'])

# %%
stats_22.head(10)

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Position,stats_22.PTS)
plt.title('Positions that scored the most points per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Position,stats_22.ORB)
plt.title('Positions that had the most offensive rebounds per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Position,stats_22.DRB)
plt.title('Positions that had the most defensive rebounds per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Position,stats_22.FTA)
plt.title('Positions that had the most freethrow attempts per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Position,stats_22.AST)
plt.title('Positions that had the most assist per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Position,stats_22.STL)
plt.title('Positions that had the most steals per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Position,stats_22.BLK)
plt.title('Positions that had the blocks per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Position,stats_22.threeP)
plt.title('Positions that had the most 3 pointers made per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Position,stats_22.twoP)
plt.title('Positions that had the most 2 pointers made per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Age,stats_22.PTS)
plt.title('Age that players scored the most points in the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_22.Age,stats_22.FGP)
plt.title('Age that players had the highest field goal percentage')

# %%
#1956 Season EDA

# %%
stats_56.PTS.plot.hist(bins=5)

# %%
stats_56 = pd.read_csv('player_stats_56.csv')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_56.Position,stats_56.PTS)
plt.title('Positions that scored the most points per game for the 1956 season')

plt.xlabel("Position")
plt.ylabel("Points Per Game")

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats_56.Position,stats_56.FGP)
plt.title('Positions with the highest field goal percentage for the 1956 season')

plt.xlabel("Position")
plt.ylabel("Field Goal Percentage")

# %%
#1979 Season

# %%
stats_79 = pd.read_csv('player_stats_79.csv')

# %%
stats_79.threePA.plot.hist(bins=30)

# %%
#1995 Season

# %%
stats_95 = pd.read_csv('player_stats_95.csv')

# %%
stats_95.threePA.plot.hist(bins=30)

# %%
stats_56.PTS.plot.hist(bins=5)

# %%
stats_22.threePA.plot.hist(bins=30)

# %%
