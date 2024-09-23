"""
    library file
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = "women-stem.csv"


def load_dataset():
    """load a dataset from input"""
    df = pd.read_csv(dataset)
    return df


def get_mean(df, col):
    """calculate the mean of selected column from dataframe"""
    return df[col].mean()


def get_median(df, col):
    """calculate the median of selected column from dataframe"""
    return df[col].median()


def get_std(df, col):
    """calculate the standard deviation of selected column from dataframe"""
    return df[col].std()


def plot_histogram(df, col):
    """plot histogram plot of selected column from import dataframe"""
    plt.figure(figsize=(12, 8))
    sns.histplot(df[col].dropna(), bins=30, kde=True)
    plt.title("Histogram of " + col)
    plt.xlabel(col)
    plt.ylabel("Population")
    plt.show()


def plot_scatter(data, x_col, y_col):
    """plot scatter plot of selected column from import dataframe"""
    data.plot.scatter(x=x_col, y=y_col)
    plt.title(x_col + " vs. " + y_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()
