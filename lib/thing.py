import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    columns = ['Zip Code', 'Month', '2018', '2017']
    dataframe = pd.read_csv('csvs/data.csv')
    dataframe = dataframe[columns]
    # pivot_2017 = dataframe.pivot('Zip Code', 'Month', '2017')
    pivot_2018 = dataframe.pivot('Zip Code', 'Month', '2018')
    f, ax = plt.subplots(figsize=(11, 15))
    sns.heatmap(pivot_2018, ax = ax)
    # dataframe = dataframe.melt(id_vars=['Zip Code', 'Month'], var_name ='Year', value_name = 'CE_Sales')
    # zip_codes = dataframe['Zip Code'].unique()

    # import pdb; pdb.set_trace()
    # print(dataframe)

    # sns.set_context("talk")
    #
    # #
    # # ax = sns.heatmap(dataframe, annot=True, fmt="d", linewidths=.5, ax=ax, xticklabels=['Jan', 'Feb', 'Mar'],
    # #                  yticklabels=zip_codes)
    # ax = sns.heatmap(dataframe)
    # ax.axes.set_title("Heatmap of Ride Counts by Day and Hour of Day", fontsize=24, y=1.01)
    # ax.set(xlabel='Day of Week', ylabel='Starting Hour of Ride');

    plt.savefig('images/2018_heatmap.png')