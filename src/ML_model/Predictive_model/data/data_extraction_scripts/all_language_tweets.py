from twitter_api import generate_data


def keywords():
    """list some words seen in tweets

    Returns:
       data(List): list of language words
    """
    data = [
        "data",
        "power",
        "politics",
        "sports",
        "church",
        "prayer",
        "money",
        "paid",
        "phone",
        "gym",
        "software",
        "AI",
        "horrifying",
        "official",
        "news",
    ]
    return data


def extract_data(data):
    """Calls the generate data function to extract tweets in the
    specified time period and saves it to disk

    Args:
        data (List): list of words
    """

    df = generate_data(data, "2022-01-01", "2023-01-28")
    df.to_csv("../data/all_language.csv")


if __name__ == "__main__":
    data = keywords()
    extract_data(data)
