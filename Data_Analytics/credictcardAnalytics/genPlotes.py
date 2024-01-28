

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# plots.
# since we have two labels we can try to draw accordingly as well
# plots.
# since we have two labels we can try to draw accordingly as well
def plot_field(df: pd.DataFrame, field_name:str):
    fig, axes = plt.subplots(1,2,figsize=(12, 5))

    # plt.figure(figsize=(8,5))
    # kde plot.
    sns.kdeplot(data=df,x=field_name, color='grey', ax=axes[0])
    axes[0].set_xlabel(f"field :{field_name}")
    axes[0].set_ylabel(f"Density")
    median = df[field_name].median()
    axes[0].set_title(f" mean:{round(df[field_name].mean(),2)} median: {median}")
    axes[0].axvline(median, color='orange', linestyle='dashed', label="median")
    axes[0].axvline(df[field_name].mean(), color='blue', linestyle='dashed', label='mean')
    axes[0].legend()

    sns.boxplot(data=df, x=field_name, ax=axes[1], orient='h')
    axes[1].set_title(f"min: {round(df[field_name].min(),2)} max:{round(df[field_name].max(),2)}")

    plt.tight_layout()
    plt.show()