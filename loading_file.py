import pandas as pd

def read_cvs(filename, **kwargs):
    return pd.read_csv(filename, **kwargs)