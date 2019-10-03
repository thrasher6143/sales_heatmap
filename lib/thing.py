import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    columns = ['Zip Code', 'Month', '2018', '2017']
    dataframe = pd.read_csv('csvs/data.csv')
    dataframe = dataframe[columns]
    dataframe = dataframe.fillna(0)
    # pivot_2017 = dataframe.pivot('Zip Code', 'Month', '2017')
    pivot_2018 = dataframe.pivot('Zip Code', 'Month', '2018')
    pivot_2018 = pivot_2018.fillna(1).astype(int)
    # pivot_2017 = pivot_2017.round()

    f, ax = plt.subplots(figsize=(15, 20))
    # ax = sns.heatmap(pivot_2017)
    sns.heatmap(pivot_2018, fmt='g', robust=True, annot=True, ax=ax, cmap="Reds", linewidths=.3, xticklabels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
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
    # ax.set(xlabel='Day of Week', ylabel='Star
    # ting Hour of Ride');

    plt.savefig('images/2018_heatmap.png')