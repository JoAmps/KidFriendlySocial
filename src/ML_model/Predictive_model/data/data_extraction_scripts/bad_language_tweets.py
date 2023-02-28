from twitter_api import generate_data
from typing import List


def keywords():
    """list some bad language words seen in tweets

    Returns:
       data(List): list of bad language words
    """
    data = [
        "fuck",
        "idiot",
        "bitch",
        "nigga",
        "fagot",
        "dick",
        "pussy",
        "cunt",
        "fucking",
        "rape",
        "whore",
    ]
    return data


def extract_data(data: List):
    """Calls the generate data function to extract tweets
    in the specified time period and saves it to disk

    Args:
        data (List): list of bad language words
    """

    df = generate_data(data, "2022-01-01", "2023-01-28")
    df = df.assign(label=lambda x: "bad_language_tweet")
    df.to_csv("../data/bad_language.csv")


if __name__ == "__main__":
    data = keywords()
    extract_data(data)
