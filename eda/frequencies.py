import pandas as pd
import matplotlib.pyplot as plt

def apply_cols(df, func):
    for c in df.columns:
        func(df, c)

def plot_frequency(df, column):
    plot = df.groupby(column).size().plot(kind='bar')
    fig = plot.get_figure()
    fig.savefig("frequency_plots/{}.png".format(column))

df = pd.read_csv("data/data.csv")
apply_cols(df, plot_frequency)

