import logging
import numpy as np
from sklearn.metrics import accuracy_score, f1_score,\
    recall_score, precision_score, confusion_matrix
import matplotlib.pyplot as plt
import itertools


# evaluate the performance of the model
def evaluate(test, trainer, test_df):
    """Evaluates the trainer performance

    Args:
        test (pandas dataframe): dataframe to be tested
        trainer (hugging face module) : module containing
                            the trained model and its functionalities
        test_df (test dataloader) : the test dataloader
    Returns:
        test (pandas dataframe): dataframe containing model prediction
    """
    try:
        # Call the summary
        predictions = trainer.predict(test_df)
        test["prediction"] = np.argmax(
            predictions.predictions, axis=1
        )
        # evaluate model
        print(trainer.evaluate())
        logging.info("SUCCESS! Evaluation completed")
        return test
    except BaseException:
        logging.info("ERROR! Evaluation not completed")


# calculate the metrics of the model and plots the confusion matrix
def calcuate_scores(test):
    """Calculates the performance and saves the required
        metrics and the confusion matrix

    Args:
        test (pandas dataframe): dataframe to be tested
        trainer (hugging face module) : module containing the
                trained model and its functionalities
        test_df (test dataloader) : the test dataloader
    Returns:
        test (pandas dataframe): dataframe containing model prediction
    """

    try:
        # evaluates the performance of the model on the test set
        f1 = f1_score(
            test["labels"],
            test["prediction"],
            average="macro",
            zero_division=1,
        )
        accuracy = accuracy_score(
            test["labels"], test["prediction"]
        )
        recall = recall_score(
            test["labels"],
            test["prediction"],
            average="macro",
            zero_division=1,
        )
        precision = precision_score(
            test["labels"],
            test["prediction"],
            average="macro",
            zero_division=1,
        )

        # joins the metrics together and saves to disk
        model_scores = []
        scores = (
            "accuracy: %s \n"
            "precision: %s \n"
            "recall: %s \n"
            "f1: %s" % (accuracy, precision, recall, f1)
        )

        model_scores.append(scores)
        with open(
            "model_performance/metrics.txt", "w"
        ) as out:
            for score in model_scores:
                out.write(score)

    except BaseException:
        logging.info("ERROR! Metrics failed to be computed")


def plot_confusion_matrix(
    cm, classes, normalize=False, title="Confusion matrix"
):
    """Plots the confusion matrix

    Args:
       cm (scikit learn module) : creates the confusion matrix
       classes (list) : names of the classes
        normalize (bool) : decides if values should be a percentage or not
        title (str) : title of confusion matrix
    Returns:
        plt (matplotlib module) :  plot of the confusion matrix
    """

    if normalize:
        cm = (
            cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]
        )
    plt.imshow(cm, interpolation="nearest")
    plt.title(title, fontsize=23)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.ylabel("True label", fontsize=10)
    plt.xlabel("Predicted label", fontsize=10)
    plt.xticks(tick_marks, classes, fontsize=9, rotation=0)
    plt.yticks(tick_marks, classes, fontsize=9)

    fmt = ".2f" if normalize else "d"
    thresh = cm.max() / 2.0

    for i, j in itertools.product(
        range(cm.shape[0]), range(cm.shape[1])
    ):
        plt.text(
            j,
            i,
            format(cm[i, j], fmt),
            horizontalalignment="center",
            color="white" if cm[i, j] < thresh else "black",
            fontsize=30,
        )

    return plt


def generate_confusion_matrix(test):
    """Generated the confusion matrix amd saves to disk

    Args:
       test (pandas dataframe): dataframe containing model prediction
    Returns:
        None
    """

    classes = [
        "bad language tweets",
        "good language tweets",
    ]
    cm = confusion_matrix(
        test["labels"], test["prediction"]
    )
    plot_confusion_matrix(
        cm,
        classes=classes,
        normalize=False,
        title="Confusion matrix",
    )

    plt.savefig(
        "images/confusion_matrix.png",
        bbox_inches="tight",
        dpi=1000,
    )
