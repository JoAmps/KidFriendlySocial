import pandas as pd
import numpy as np


def load_data(ucberkerley, all_language, bad_language):
    """Loads csv files

    Args:
        ucberkerley (csv file): csv file containing data
                                from hugging face dataset
        all_language (csv file): csv file containing data
                                from twitter api on certain keywords
        bad_language (csv file): csv file containing data from twitter
                                 api on certain bad language keywords

    Returns:
        3 pandas dataframes: pandas dataframe of the 3 csv files
    """

    df_berkeley = pd.read_csv(ucberkerley)
    df_all_language = pd.read_csv(all_language)
    df_bad_language = pd.read_csv(bad_language)
    return df_berkeley, df_all_language, df_bad_language


def rename_columns(df_berkeley, df_all_language):
    """Selects the relevant columns and renames the columns
     into the appropriate format

    Args:
        df_berkeley (pandas dataframe): pandas dataframe of
                                        the ucberkerly dataset
        df_all_language (pandas dataframe): pandas dataframe of
                                            the all language dataset

    Returns:
        pandas dataframe: the two pandas dataframe
                            after renaming the columns
    """

    df_berkeley = df_berkeley[["text", "hate_speech_score"]]
    df_berkeley = df_berkeley.rename(
        columns={
            "text": "tweet",
            "hate_speech_score": "label",
        }
    )

    df_all_language = df_all_language[["text", "label"]]
    df_all_language = df_all_language.rename(
        columns={"text": "tweet"}
    )
    return df_berkeley, df_all_language


def create_labels(df_berkeley):
    """Generates the binary labels using the threshold
        of 0.5(below-good language, above-bad language)

    Args:
        df_berkeley (pandas dataframe): processed pandas dataframe
                                         of the ucberkerly dataset

    Returns:
        pandas dataframe: pandas dataframe with the labels computed
    """

    df_berkeley["label"] = np.where(
        df_berkeley["label"] < 0.5,
        "good language tweet",
        "bad_language_tweet",
    )
    return df_berkeley


def merge_datasets(
    df_berkeley, df_all_language, df_bad_language
):
    """_summary_

    Args:
        df_berkeley (pandas dataframe): processed ucberkerly pandas dataframe
        df_all_language (pandas dataframe): processed all language
                                            pandas dataframe
        df_bad_language (pandas dataframe):  processed bad language
                                            pandas dataframe

    Returns:
        pandas dataframe: combined pandas dataframe
    """

    datasets = [
        df_all_language,
        df_bad_language,
        df_berkeley,
    ]
    datasets = pd.concat(datasets)
    print(
        (datasets["label"].value_counts(normalize=True)) * 100
    )
    datasets.to_csv("../data/final_dataset.csv")
    return datasets


if __name__ == "__main__":
    (
        df_berkeley,
        df_all_language,
        df_bad_language,
    ) = load_data(
        "../data/data-ucberkeley-dlab.csv",
        "../data/annotated_all_language.csv",
        "../data/bad_language.csv",
    )
    df_berkeley, df_all_language = rename_columns(
        df_berkeley, df_all_language
    )
    df_berkeley = create_labels(df_berkeley)
    datasets = merge_datasets(
        df_berkeley, df_all_language, df_bad_language
    )
