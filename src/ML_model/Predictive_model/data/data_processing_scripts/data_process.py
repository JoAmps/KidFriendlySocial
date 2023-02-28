import pandas as pd
import re
import warnings
import logging
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")
pd.options.display.float_format = "{:,.2f}".format


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


# process the loaded data
def load_data(path_of_dataset):
    """Loads data and applies the clean function

    Args:
        path_of_dataset (path): path to the dataset

    Returns:
        df (pandas dataframe): dataframe with the tweets cleaned
    """

    try:
        df = pd.read_csv(path_of_dataset)
        df = df[["tweet", "label"]]
        df["tweet"] = df["tweet"].apply(tweets_cleaner)
        df = df.rename(
            columns={"tweet": "text", "label": "labels"}
        )
        logging.info(
            f"SUCCESS! : Data Succesfully loaded, tweets cleaned\
              and there are {len(df)} number of rows"
        )
        return df
    except BaseException:
        logging.info("Error!: Data could not be loaded")


# process the target data
def process_target(df):
    """Binarizes the labels by converting from texts to numerical format

    Args:
        df (pandas dataframe): dataframe of processed data

    Returns:
        df (pandas dataframe): dataframe with the labels binarized
    """

    try:
        binarizer = LabelBinarizer()
        df["labels"] = binarizer.fit_transform(df["labels"])
        logging.info(
            f"SUCCESS! : Labels successfully encoded and label 1 contains\
            {(df['labels'].value_counts(normalize=True).values[0])*100}\
            % and label 0 contains \
            {(df['labels'].value_counts(normalize=True).values[1])*100}%"
        )
        return df
    except BaseException:
        logging.info("Error!: Labels not encoded!")


# split the datasets
def split_datasets(df):
    """splitting the datasets for training, validation
        and testing by stratifying the labels column

    Args:
        df (pandas dataframe): processed pandas dataframe

    Returns:
        train (pandas dataframe) , test (pandas dataframe),
        validation_df (pandas dataframe): the split dataset
    """
    try:
        train, testvalidation = train_test_split(
            df,
            test_size=0.2,
            stratify=df["labels"],
            random_state=0,
        )
        test, validation_df = train_test_split(
            testvalidation,
            test_size=0.5,
            stratify=testvalidation["labels"],
            random_state=0,
        )
        logging.info(
            f"SUCCESS! : Dataset split succesfully and there \
            {len(train)} train examples, {len(validation_df)} \
            validation examples and {len(test)} test examples"
        )
        return train, validation_df, test
    except BaseException:
        logging.info("Error!: Dataset not split")
