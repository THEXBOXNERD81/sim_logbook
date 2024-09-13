import pytest
import pandas as pd

import sql_connection as sql
import csv_loading_and_cleaning as csv

@pytest.fixture
def testing_df():
    df = csv.load_logbook('Test3.csv')
    return df

def test_load_logbook(testing_df):
    assert isinstance(testing_df, pd.DataFrame)


def test_converting_dtypes(testing_df):
    df = csv.converting_dtypes(testing_df)
    assert isinstance(df, pd.DataFrame)

