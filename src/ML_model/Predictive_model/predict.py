from transformers import pipeline
import re

model = "bad_language_tweets_detector"


# function to clean the tweets
def tweets_cleaner(x):
    """Cleans the tweets

    Args:
        x (str): Raw tweets

    Returns:
        x (str): Cleaned tweets
    """
    x = x.lower()
    x = x.encode("ascii", "ignore").decode("unicode_escape")
    x = re.sub(r"\xa0", " ", x)
    x = re.sub(r"&amp", " ", x)
    x = re.sub(r"&gt", " ", x)
    x = re.sub(r"@[\w]+", "", x)
    return x


def load_model_and_tokenizer(tokenizer, model):
    """
    Loads tokenizer and model

    Args:
        tokenizer(str) : name of the tokenizer
        model_name (str) : name of the transformer model
    Returns
        bad_language_detection_pipeline (hugging face pipeline)
                         : prediction pipeline
    """
    bad_language_detection_pipeline = pipeline(
        "text-classification",
        model=model,
        tokenizer=tokenizer,
    )
    return bad_language_detection_pipeline


def predict_language_quality(
    tweet, bad_language_detection_pipeline
):
    """
    Takes the tweet input, processes it and returns the
            quality of language used in the tweet

    Args:
        tweet (str): input tweet by user

    Returns
        classifier (dict): predicton result with label and confidence score
    """

    text = tweets_cleaner(tweet)
    classifier = bad_language_detection_pipeline(text)
    if classifier[0]["label"] == "LABEL_0":
        return tweet, classifier[0]["label"]
    else:
        return tweet, classifier[0]["label"]
