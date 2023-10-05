#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %%
data = pd.read_csv("Data_Analytics/Data/NFL_2017.csv")
print(data.columns)
# %%
# filtering
# data = data[data['Season'] == 2009]
date = data['Date'].unique()
df = pd.DataFrame(date, columns=['Date'])

# %%
df['Date'] = pd.to_datetime(df['Date'])
# %%
# getting the week
df['week'] = df['Date'].dt.strftime('%Y-W%V')
# %%
df['month'] = df['Date'].dt.strftime("M%m")
# inference : start form month 09 and end in month 12
# %%
df['Year'] = df['Date'].dt.strftime("%Y")
# %%
# quarter values
df['Quarter'] = df['Date'].dt.to_period('Q').dt.strftime("%q")
# %%
