from __future__ import annotations

from typing import TYPE_CHECKING, Optional
import pandas as pd

if TYPE_CHECKING:
    from pyspark.sql import SparkSession, DataFrame

def file_loader(session: SparkSession, path: str, schema_info: Optional[bool] = False):
    """Loads the file from the given path, generate schema info according to the value of schema_info

    Args:
        session : current spark session object
        path: Path to locate the file.
        schema_info: whether to generate schema of the loaded file.
    
    Returns:
        df: loaded data frame
        schema_df (pd.Dataframe) if schema_info true.
    """
    df = session.read.csv(path, header=True, inferSchema=True)
    if not schema_info:
        return df
    #TODO : implementation of schema information.
    return
