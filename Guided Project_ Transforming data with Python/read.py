import pandas as pd

def load_data():
    df = pd.read_csv("hn_stories.csv")
    df.columns = ['submission_time', 'upvotes','url','headline']
    print(df[0:5][['url']])
    return df
