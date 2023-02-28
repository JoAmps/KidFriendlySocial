from Predictive_model.data.data_processing_scripts.data_process import (
    load_data,
    process_target,
    split_datasets,
)
import pytest
import warnings

warnings.filterwarnings("ignore")


@pytest.fixture
def data():
    """
    Obtain data
    """
    df = load_data(
        "Predictive_model/data/data/final_dataset.csv"
    )
    return df


def test_required_num_labels(data):
    """
    Check labels is binary
    """
    df = process_target(data)
    assert len(set(df["labels"])) == 2


def test_num_rows_in_splits(data):
    """
    Check train data has the most data
    """
    train, validation_df, test = split_datasets(data)
    assert len(train) > (len(validation_df) + len(test))
