"""
Test goes here

"""

from hello import (
    get_describe,
    col_summ_stats,
    generate_visualization,
    save_to_md,
)


def test_get_describe():
    test_describe = get_describe()
    assert test_describe.shape == (8, 7)


def test_col_summ_stats():
    col = "ShareWomen"
    womenstem_data_describe = get_describe()
    summ_stats_dictionary = col_summ_stats(col)
    assert (
        womenstem_data_describe.loc["mean", "ShareWomen"]
        == summ_stats_dictionary["mean"]
    )
    assert (
        womenstem_data_describe.loc["50%", "ShareWomen"]
        == summ_stats_dictionary["median"]
    )
    assert (
        womenstem_data_describe.loc["std", "ShareWomen"] == summ_stats_dictionary["std"]
    )


if __name__ == "__main__":
    test_get_describe()
    test_col_summ_stats()
