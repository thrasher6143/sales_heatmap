import csv
import pandas as pd


def run():
    columns = ['Zip Code', 'Month', '2018', '2017']
    dataframe = pd.read_csv('csvs/data.csv')
    dataframe = dataframe[columns]
    dataframe = dataframe.melt(id_vars=['Zip Code', 'Month'], var_name ='Year', value_name = 'CE_Sales')

    import pdb; pdb.set_trace()
    print(dataframe)