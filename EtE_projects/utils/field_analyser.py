# pass a data field : pd.Series. give the information back
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def _analyse(ds:pd.Series):
    '''
    
    '''
    print("data type  :", ds.dtypes)
    pass



def missing_stats(df:pd.DataFrame)->pd.DataFrame:
    """ The following function will create a report of missing values
    
    """
    missing_count = df.isnull().sum()
    total_missing_cols_count = (missing_count >0).sum()
    print("total missing fields count: ", total_missing_cols_count)
    total_missing_values:int = missing_count.sum()
    if not total_missing_values:
        return "No missing values"
    print("Total values missing: ", total_missing_values)
    missing_percentage = round(df.isnull().mean() * 100, 2)
    # creating the meta data frame
    meta_df = pd.DataFrame({
        "Missing Values": missing_count,
        "Missing Percentage": missing_percentage
    })
    plt_df = meta_df[meta_df['Missing Values'] > 0]
    plt_df['Missing Percentage'].sort_values(ascending=False).plot(kind='bar')
    plt.show()
    return meta_df.sort_values(by="Missing Values", ascending=False)


def target_analyser_with_na_fields(df:pd.DataFrame, col_name:str):
    """ Create plots to understand relationship with missing field
    with the target.
    
    """
    df = df.copy()
    df[col_name] = np.where(df[col_name].isnull(), 1,0)
    # 1 => missing 0 => not missing
    tmp_df = df.groupby(col_name)['SalePrice'].agg(['mean', 'std'])
    tmp_df.plot(kind="barh", y="mean", xerr='std')
    plt.show()
