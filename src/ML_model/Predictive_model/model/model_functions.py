import pandas as pd
import torch
import datasets
import warnings
import logging
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification,\
    Trainer, TrainingArguments

warnings.filterwarnings("ignore")
pd.options.display.float_format = "{:,.2f}".format


# function to tokenize the dataset
def tokenization(batched_text, tokenizer):
    """Function to Tokenize the tweets

    Args:
        batched_text (pandas series): tweets column
        tokenizer (str) : name of the tokenizer

    Returns:
        tokens (str) : tokenized texts
    """

    tokens = tokenizer(
        batched_text["text"], padding=True, truncation=True
    )
    return tokens


# function to compute the metrics
def compute_metrics_for_classification(pred):
    """Validates the trained model using accuracy and F1.

    Args:
        pred (pandas series): predictions from the trained model

    Returns:
        accuracy (float) : number of correct predictions
                     over total number of samples
        f1 (float): harmonic mean of precision and recall
    """
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    f1 = f1_score(
        labels, preds, average="macro", zero_division=1
    )
    acc = accuracy_score(labels, preds)
    return {"accuracy": acc, "f1": f1}


# create pytorch data loaders and find the max_length
def create_loaders(train, validation_df, test, model_name):
    """Creates pytorch dataloaders for train, validation and test datasets

    Args:
        train (pandas dataframe) : training dataframe
        validation_df (pandas dataframe) : validation dataframe
        test (pandas dataframe) : test dataframe
        model_name (str) : name of the transformer model

    Returns:
        train (pandas datasets) : pandas datasets module
        validation_df (pandas dataframe) : pandas datasets module
        test_df (pandas dataframe) : pandas datasets module
        token_lens : the number of tokens for every tweet
    """

    try:
        tokenizer = AutoTokenizer.from_pretrained(
            model_name, model_max_length=512
        )
        # finding the maximum length of the tweets
        token_lens = []
        for content in train["text"]:
            tokens = tokenizer.encode(
                content, max_length=512, truncation=True
            )
            token_lens.append(len(tokens))

        tokenizer = AutoTokenizer.from_pretrained(
            model_name, model_max_length=np.max(token_lens)
        )
        train = datasets.Dataset.from_pandas(train)
        test_df = datasets.Dataset.from_pandas(test)
        validation_df = datasets.Dataset.from_pandas(
            validation_df
        )

        # tokenization of train, test and validation
        train = train.map(
            lambda x: tokenization(x, tokenizer),
            batched=True,
            batch_size=train.shape[0],
        )
        test_df = test_df.map(
            lambda x: tokenization(x, tokenizer),
            batched=True,
            batch_size=test_df.shape[0],
        )
        validation_df = validation_df.map(
            lambda x: tokenization(x, tokenizer),
            batched=True,
            batch_size=validation_df.shape[0],
        )

        # selecting only the relevant columns for training
        train.set_format(
            "torch",
            columns=[
                "input_ids",
                "attention_mask",
                "labels",
            ],
        )
        test_df.set_format(
            "torch",
            columns=[
                "input_ids",
                "attention_mask",
                "labels",
            ],
        )
        validation_df.set_format(
            "torch",
            columns=[
                "input_ids",
                "attention_mask",
                "labels",
            ],
        )

        logging.info(
            "SUCCESS! : Data Loaders created successfully"
        )
        return train, validation_df, test_df, token_lens
    except BaseException:
        logging.info(
            "Error!: Error occurred when creating data loaders"
        )


# Specifiy the arguments for the trainer
def train_model(model_name, train, validation_df):
    """Trains the models

    Args:
        model_name (str) : name of the transformer model
        train (pandas datasets) : pandas datasets module
        validation_df (pandas datasets) : pandas datasets module

    Returns:
        trainer (hugging face module) : module containing
                    the trained model and its functionalities
    """

    # setting the arguments
    try:
        num_epochs = 5
        training_args = TrainingArguments(
            output_dir="./logs/model_name",
            logging_dir="./logs/runs",
            num_train_epochs=num_epochs,
            per_device_train_batch_size=64,
            per_device_eval_batch_size=64,
            weight_decay=0.01,
            learning_rate=5e-5,
            save_total_limit=10,
            load_best_model_at_end=True,
            evaluation_strategy="epoch",
            save_strategy="epoch",
        )
        # whether gpu would be used
        if torch.cuda.is_available():
            torch.device("cuda")
        else:
            torch.device("cpu")

        # instantiating the model and datasets
        trainer = Trainer(
            model=AutoModelForSequenceClassification.from_pretrained(
                model_name, num_labels=2, return_dict=True
            ),
            args=training_args,
            train_dataset=train,
            eval_dataset=validation_df,
            compute_metrics=compute_metrics_for_classification,
        )
        # Train and save the model
        trainer.train()
        trainer.save_model(
            "model/trained_models/bad_language_tweets_detector"
        )

        logging.info("Success! : Data successfully trained")
        return trainer
    except BaseException:
        logging.info("Error! Error in training pipeline")
