import pandas as pd
def convert_to_long_format(df):
    long=df.melt(id_vars=["Jahr","Monat"], var_name="Bundesländer", value_name="Temperatur")
    return long