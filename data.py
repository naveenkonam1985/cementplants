import pandas as pd


def cement_plants_data():
    url_latest = './static/Cement_Plants_in_India.csv'
    df = pd.read_csv(url_latest, encoding = "ISO-8859-1", engine='python')
    return(df)



