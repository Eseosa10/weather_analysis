import pandas as pd
from pathlib import Path

def load_monthly_file(path):
    df=pd.read_csv(path, sep=";", skiprows=1)
    return df

def load_all_monthly_files(dir_path):
    dataframes=[]
    files =Path(dir_path).glob("regional_averages_tm_*.txt")

    for file in files:
        df_data=load_monthly_file(file)
        dataframes.append(df_data)
    combines_df=pd.concat(
        dataframes,
        ignore_index=True
    )

    return combines_df