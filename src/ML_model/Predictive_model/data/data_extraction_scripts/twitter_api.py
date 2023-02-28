import snscrape.modules.twitter as sntwitter
import pandas as pd
from typing import List


def generate_data(data: List, from_date: str, to_date: str):
    """To generate tweets from certain keywords in a specified time period

    Args:
        data (List): list of keywords to use to extract data
        from_date (str): start date to generate tweets
        to_date (str): end date to generate tweets

    Returns:
        df(pandas dataframe): dataframe containing tweets
    """

    print(data)
    tweets_list = []
    for j in data:
        for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(
                f"{j} since:{from_date} until:{to_date}"
            ).get_items()
        ):
            if i > 100:
                break
            tweets_list.append(
                [
                    tweet.date,
                    tweet.rawContent,
                    tweet.user.username,
                    tweet.retweetCount,
                    tweet.likeCount,
                    j,
                ]
            )
            df = pd.DataFrame(
                tweets_list,
                columns=[
                    "date",
                    "tweet",
                    "username",
                    "retweets",
                    "likes",
                    "keyword",
                ],
            )
    print(len(df))
    return df
