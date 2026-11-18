import pandas as pd
import numpy as np
def check_missing(df):
    anzahl_fehlende=df.isna().sum()
    result=anzahl_fehlende[anzahl_fehlende > 0]
    return result
def check_duplicated(df):
    list_duplicates=df.duplicated().sum()
    result=list_duplicates[list_duplicates>0]
    return result

def check_empty_col(df):
    empty_cols=df.columns[df.notna().sum()==0]
    
    return list(empty_cols)

def check_datatypes(df):
    return df.dtypes


def check_temperature_ranges(df,
                             min_temp=-50,
                             max_temp=50):

    temperature_columns = df.select_dtypes(
        include=["float64"]
    )

    invalid_values = {}

    for column in temperature_columns.columns:

        invalid = temperature_columns[
            (temperature_columns[column] < min_temp)
            |
            (temperature_columns[column] > max_temp)
        ]

        if not invalid.empty:
            invalid_values[column] = invalid[
                column
            ].tolist()

    return invalid_values