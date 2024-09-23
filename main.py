"""
Main cli or app entry point
"""

from mylib.calculator import (
    load_dataset,
    get_mean,
    get_median,
    get_std,
    plot_histogram,
    plot_scatter,
)


def get_describe():
    """get dataset"""
    data = load_dataset()
    return data.describe()


def col_summ_stats(col):
    """generate the summary of the statistic data"""
    data = load_dataset()
    mean = get_mean(data, col)
    median = get_median(data, col)
    std = get_std(data, col)
    print(f"Column of Interest: {col}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std}")
    return {"mean": mean, "median": median, "std": std}


def generate_visualization(col, col2):
    """generate histogram and scatter plot"""
    data = load_dataset()
    plot_histogram(data, col)
    plot_scatter(data, col, col2)


def save_to_md():
    """save result to a markdown file"""
    with open("test.md", "a") as file:
        file.write("test")


if __name__ == "__main__":
    print(get_describe())
    col_of_intrst = "ShareWomen"
    compare_col = "Total"
    col_summ_stats(col_of_intrst)
    generate_visualization(col_of_intrst, compare_col)
