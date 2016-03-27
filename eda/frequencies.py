import math

import pandas as pd
import matplotlib.pyplot as plt


def plot_frequencies(df):
    def apply_cols(df, func):
        for c in df.columns:
            func(df, c)

    def plot_frequency(df, column):
        plot = df.groupby(column).size().plot(kind='bar')
        plot.set_xlabel("")
        fig = plot.get_figure()
        fig.suptitle(column)
        fig.savefig("frequency_plots/{}.png".format(column))

    apply_cols(df, plot_frequency)

def plot_frequencies_digest(df):
    def apply_cols(df, func):
        for (i, c) in enumerate(df.columns):
            plot_frequency(df, i, c)

    def plot_frequency(df, i, column):
        row = math.floor(i / ncols)
        col = i % ncols
        cell = ax[row, col]
        
        df.groupby(column).size().plot(
          ax=cell,
          kind='bar')
        cell.set_title(column)
        cell.set_xlabel("")
        

    ncols = 4
    nrows = math.floor(len(df.columns) / ncols + 1)
    fig, ax = plt.subplots(figsize=(40,40), nrows=7, ncols=4)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    apply_cols(df, plot_frequency)
    fig.savefig("frequency_plots/frequencies_digest.png")

df = pd.read_csv("data/data.csv")
plot_frequencies(df)
plot_frequencies_digest(df)
