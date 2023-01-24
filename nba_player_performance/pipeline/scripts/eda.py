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
import pandas as pd
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# # %matplotlib inline
import matplotlib.pyplot as plt  # Matlab-style plotting
import seaborn as sns
stats = pd.read_csv(upstream['clean']['data'])

# %%
stats.head(10)

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats.Position,stats.PTS)
plt.title('Positions that scored the most points per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats.Position,stats.ORB)
plt.title('Positions that had the most offensive rebounds per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats.Position,stats.DRB)
plt.title('Positions that had the most defensive rebounds per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats.Position,stats.FTA)
plt.title('Positions that had the most freethrow attempts per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats.Position,stats.AST)
plt.title('Positions that had the most assist per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats.Position,stats.STL)
plt.title('Positions that had the most steals per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats.Position,stats.BLK)
plt.title('Positions that had the blocks per game for the 2022 season')

# %%
plt.figure(figsize=(10, 5))
plt.bar(stats.Position,stats.threeP)
plt.title('Positions that had the most 3 pointers made per game for the 2022 season')

# %%
