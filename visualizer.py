import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import preprocessor

df = preprocessor.preprocess()

def draw_line_plot():
    plt.figure(figsize=(15,8))
    sns.lineplot(x="date", y="value", color="r", data=df);
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019");
    plt.ylabel("Page Views");
    plt.xlabel("Date");
    
def draw_bar_plot():
    df_res = df.reset_index()
    plt.figure(figsize=(8,6));
    sns.barplot(x=df_res.date.dt.year, y=df_res.value, hue=df_res.date.dt.month, palette="tab10");
    plt.xlabel("Years");
    plt.ylabel("Average Page Views");
    plt.legend(title="Month");
    
def draw_box_plot():
    plt.subplot(1,2,1);
    df_res = df.reset_index()
    sns.boxplot(x=df_res.date.dt.year, y=df_res.value);
    plt.title("Year-Wise Boxplot (Trend)");
    plt.xlabel("Year");
    plt.ylabel("Page Views");

    df_res['month'] = [d.strftime('%b') for d in df_res.date]
    plt.subplot(1,2,2);
    sns.boxplot(x=df_res.month, y=df_res.value);
    plt.title("Month-Wise Boxplot (Seasonality)");
    plt.xlabel("Month");
    plt.ylabel("Page Views");

    plt.subplots_adjust(left=9, right=11);