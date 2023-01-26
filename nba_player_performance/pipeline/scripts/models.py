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
stats = stats.drop(['Player Name', 'Position', 'Team'], axis=1)

# %%
stats.dtypes


# %%
stats.columns

# %%
X = stats[['threePA','MP']]

# %%
y = stats['PTS']

# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101) 

# %%
from sklearn.linear_model import LinearRegression

# %%
lm = LinearRegression()
lm.fit(X_train,y_train)

# %%
model = lm

# %%
predictions = lm.predict(X_test)

# %%
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# %%
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# %%
print (mse)
print (mae)
print (r2)

# %%
import pickle
pickle.dump(lm,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

# %%
