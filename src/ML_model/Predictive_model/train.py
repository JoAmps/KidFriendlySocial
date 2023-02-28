from data.data_processing_scripts.data_process import (
    load_data,
    process_target,
    split_datasets,
)
from model.model_functions import (
    create_loaders,
    train_model,
)
from model.model_evaluations import (
    evaluate,
    calcuate_scores,
    generate_confusion_matrix,
)
import logging


# set the file and format to log every function
logging.basicConfig(
    filename="logging.log",
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


if __name__ == "__main__":
    df = load_data("data/data/final_dataset.csv")
    df = process_target(df)
    train, validation_df, test = split_datasets(df)
    (
        train,
        validation_df,
        test_df,
        token_lens,
    ) = create_loaders(
        train, validation_df, test, "vinai/bertweet-base"
    )
    trainer = train_model(
        "vinai/bertweet-base", train, validation_df
    )
    test = evaluate(test, trainer, test_df)
    calcuate_scores(test)
    generate_confusion_matrix(test)
