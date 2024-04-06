import pandas as pd

def read_file(filename, **kwargs):
    return pd.read_csv(filename, **kwargs)