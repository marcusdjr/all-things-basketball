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
upstream = ['clean']

# This is a placeholder, leave it as None
product = None


# %%
import pandas as pd
import numpy as np
pbp_stats_22 = pd.read_csv(upstream['clean']['data'])

# %%
pbp_stats_22.head(20)

# %%
#Feature Selection

# %%
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest,chi2

# %%
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Split the data into features (X) and target (y)
X = pbp_stats_22.drop(['On-Off','Player','Position','Team','PGP','SGP','SFP','PFP',], axis=1)
y = pbp_stats_22['On-Off']

# Fit a linear regression model to the data
lm = LinearRegression()
lm.fit(X, y)

# Check if the length of lm.coef_ is equal to the length of X.columns
if len(lm.coef_) == len(X.columns):
    # Create a pandas Series from lm.coef_ and X.columns
    lm_feature = pd.Series(lm.coef_, index=X.columns)
    
    lm_feature.nlargest(10).plot(kind='barh')
else:
    print("The length of lm.coef_ does not match the length of X.columns.")

# %%
X = pbp_stats_22[['BadPass','LostBall','Shoot']]
y = pbp_stats_22[['On-Off']]

# %%
from sklearn.linear_model import LinearRegression

# %%
lm = LinearRegression()
lm.fit(X,y)

# %%
lm.coef_

# %%
lm_feature = pd.Series(lm.coef_, index=X.columns)
lm_feature.nlargest(10).plot(kind='barh')

# %%
