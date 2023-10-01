#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %%
data = pd.read_csv("Data_Analytics/Data/NFL_2017.csv")
print(data.columns)
# %%
# filtering
data = data[data['Season'] == 2009]
date = data['Date'].unique()
df = pd.DataFrame(date, columns=['Date'])

# %%
df['Date'] = pd.to_datetime(df['Date'])
# %%
# getting the week
df['week'] = df['Date'].dt.strftime('%Y-W%V')
# %%
df['month'] = df['Date'].dt.strftime("%Y-M%M")
# %%
