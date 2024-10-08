# this is a basic functions lib.
# summerize the process done.
import pandas as pd
from typing import List

num_discrete_features = ['Year_Birth', 'Kidhome', 'Teenhome',
                        'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
                        'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2',
                        'Response', 'Complain']

class DataOps:
    def __init__(self, path) -> None:
        self.df = pd.read_csv(path)
    def clean_data(self, inplace=False) -> None:
        """modify the df"""
        df = self.df.copy()
        df_transformed = (df
                .pipe(self._parse_column_names)
                .pipe(self._parse_income_from_str, "Income")
        )
        if inplace:
            self.df = df_transformed
            return None
        return df_transformed

    @staticmethod
    def _parse_column_names(df):
        df.columns = df.columns.str.strip()
        return df

    @staticmethod
    def _parse_income_from_str(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
        print("data type of the given", df[column_name].dtype)
        df[column_name] = df[column_name].str.strip().str.replace('$', '').str.replace(',', '')
        df[column_name] = df[column_name].astype("float")
        print("Income field type casted.")
        return df
    @property
    def numeric_fields(self, non_numeric=["ID"]):
        # continuos features.
        numeric_fields = list(self.df.select_dtypes("number").columns)
        numeric_fields.remove(*non_numeric)
        return [
            feature for feature in numeric_fields if feature not in num_discrete_features
        ]
    
    @property
    def categorical_features(self)->List:
        return list(self.df.select_dtypes("object").columns)
    
    @property
    def discrete_features(self):
        return num_discrete_features


    def apply_imputation(self)->pd.DataFrame:
        """
        The imputation are done based on  K
        """
        pass



class Univariate:
    def __init__(self) -> None:
        pass

    @staticmethod
    def numeric_field_types(df:pd.DataFrame, count_threshold:int=20, ratio_threshold:int=0.1):
        numeric_df = df.select_dtypes(include=["integer"])
        discrete_cols = []
        continuous_cols = []
        for field in numeric_df.columns:
            column = df[field]
            unique_values = column.nunique()
            unique_ratio = unique_values / len(column)
            if unique_values <= count_threshold or unique_ratio < ratio_threshold:
                discrete_cols.append(field)
            else:
                continuous_cols.append(field)
        return continuous_cols, discrete_cols
    

