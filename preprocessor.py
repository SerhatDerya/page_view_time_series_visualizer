import pandas as pd

def preprocess():
    
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = ["date"]).set_index("date")
    
    df = df[df["value"] > df["value"].quantile(0.025)]

    df = df[df["value"] < df["value"].quantile(0.975)]
    
    return df


