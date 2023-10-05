import pandas as pd


def load_data():
    dataframe = pd.read_excel('data/example.xlsx')
    return dataframe
