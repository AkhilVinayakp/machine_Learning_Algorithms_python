# contains different fns for plotting
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def plotTemporal_correlation(df:pd.DataFrame, col_name:str, return_info_table:bool=False)->tuple:
    """ Return a plot with 
    x-axis contains the Year sold
    y-axis (first) : contains the Sale price
    y-axis (second): contains the age of the home

    Args
    ----
    df: input data frame
    col_name: from which col we need to calculate the age.
    return_info_table: (bool) default false whether need to return
    the meta table build inside the function,

    Returns:
        tuple ( None, plt) if the return_info_table is false
              (pd.Dataframe, plt)  other wise
    
    """
    df = df.copy()
    age_from = f"age from {col_name}"
    df[age_from] = df['YrSold'] - df[col_name]
    df_temp = df.groupby("YrSold")[[age_from, 'YrSold', 'SalePrice']].median()
    fig, ax1 = plt.subplots()
    plt.ioff() # to turn off auto plotting. # TODO not working why
    x = df_temp['YrSold']
    y1 = df_temp['SalePrice']
    y2 = df_temp[age_from]

    ax1.plot(x, y1, 'g-')
    ax1.set_xlabel("Year Sold")
    ax1.set_ylabel("Sale Price", color='g')
    ax1.tick_params(axis='y', labelcolor='g') 

    ax2 = ax1.twinx()
    ax2.plot(x,y2,'b-')
    ax2.set_ylabel(age_from, color='b')
    ax2.tick_params(axis='y', labelcolor='b')

    plt.title(f"Age from {age_from} Vs Sale Price")
    # plt.close() # ? this should close the plot automatically

    if not return_info_table:
        return None, fig
    else:
        return df_temp, fig


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