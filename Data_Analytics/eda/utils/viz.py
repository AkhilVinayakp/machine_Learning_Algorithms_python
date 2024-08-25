
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List



def gen_corr_plot(df:pd.DataFrame, columns:List[str]):
    """
    Plots the correlation with heat map.
    """
    df_temp = df.copy()
    if columns:
        df_temp = df_temp[columns]
    corr_ = df_temp.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.show()
