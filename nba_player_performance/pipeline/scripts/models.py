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
upstream = ['features']

# This is a placeholder, leave it as None
product = None


# %%
import pandas as pd
stats = pd.read_csv(upstream['features']['data'])

# %%
stats.columns

# %%
X = stats[['FG','FGP','threeP','threePA','twoP','twoPA','twoPP','PTS']]

# %%
y = stats['projected_points_per_game']

# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101) 

# %%
from sklearn.linear_model import LinearRegression

# %%
from fancyimpute import MICE

# Select the column 'projected_points_per_game' from the dataset
X = df[['projected_points_per_game']]

# Create an instance of the MICE class
mice = MICE()

# Perform the imputation
imputed_data = mice.complete(X)

# %%
#lm = LinearRegression()
#lm.fit(X_train,y_train)

# %%

# %%
