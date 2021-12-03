import pandas as pd


def cement_plants_data():
    url = '~/Desktop/factoryquest/FactoryQuest/cementplants_sample.csv'
    df = pd.read_csv(url, encoding = "ISO-8859-1", engine='python')
    return(df)



