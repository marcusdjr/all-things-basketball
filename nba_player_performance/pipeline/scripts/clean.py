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
upstream = ['get']

# This is a placeholder, leave it as None
product = None


# %%
import pandas as pd
#2022 season
stats_22 = pd.read_csv(upstream['get']['data'])

# %%
stats_22.isnull().sum()

# %%
stats_22 = stats_22.dropna()

# %%
stats_22.isnull().sum()

# %%
stats_22.to_csv(product['data'], index=False)

# %%
#1956 season
stats_56 = pd.read_csv('player_stats_56.csv')

# %%
stats_56.isnull().sum()

# %%
stats_56 = stats_56.dropna(how='all')

# %%
stats_56.isnull().sum()

# %%
stats_56.head(20)

# %%
stats_56.to_csv('player_stats_56.csv')

# %%
#1979 season
stats_79 = pd.read_csv('player_stats_79.csv')

# %%
stats_79.isnull().sum()

# %%
stats_79 = stats_79.dropna()

# %%
stats_79.isnull().sum()

# %%
stats_79.head(20)

# %%
#1995 season
stats_95 = pd.read_csv('player_stats_95.csv')

# %%
stats_95.isnull().sum()

# %%
stats_95 = stats_95.dropna()

# %%
stats_95.isnull().sum()

# %%
stats_95.head(20)

# %%
#2022 season play-by-play stats
import pandas as pd
#2022 season
pbp_stats_22 = pd.read_csv(upstream['get']['data'])

pbp_stats_22['PGP'] = pbp_stats_22['PGP'].str.replace('%', '').astype(float)
pbp_stats_22['SGP'] = pbp_stats_22['SGP'].str.replace('%', '').astype(float)
pbp_stats_22['SFP'] = pbp_stats_22['SFP'].str.replace('%', '').astype(float)
pbp_stats_22['PFP'] = pbp_stats_22['PFP'].str.replace('%', '').astype(float)

# %%
pbp_stats_22.isnull().sum()

# %%
pbp_stats_22 = pbp_stats_22.dropna()

# %%
pbp_stats_22.isnull().sum()

# %%
pbp_stats_22.head(20)

# %%
pbp_stats_22.to_csv(product['data'], index=False)

# %%

# %%
