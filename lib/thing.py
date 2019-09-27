import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    columns = ['Zip Code', 'Month', '2018', '2017']
    dataframe = pd.read_csv('csvs/data.csv')
    dataframe = dataframe[columns]
    dataframe = dataframe.melt(id_vars=['Zip Code', 'Month'], var_name ='Year', value_name = 'CE_Sales')

    # import pdb; pdb.set_trace()
    print(dataframe)

    Index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
    Cols = ['A', 'B', 'C', 'D']
    df = pd.DataFrame(abs(np.random.randn(5, 4)), index=Index, columns=Cols)

    sns.heatmap(df, annot=True)
    plt.savefig('images/heatmap.png')