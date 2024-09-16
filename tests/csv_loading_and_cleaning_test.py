import pytest
import pandas as pd

from modules import csv_loading_and_cleaning as csv

@pytest.fixture
def testing_df():
    df = csv.load_logbook('csv_files/Test3.csv')
    return df

def test_load_logbook(testing_df):
    assert isinstance(testing_df, pd.DataFrame)


def test_converting_dtypes(testing_df):
    df = csv.converting_dtypes(testing_df)
    assert isinstance(df, pd.DataFrame)

def test_convert_wrong_dtypes():
    df = pd.DataFrame({'Aircraft Name': ['x', 2], 'Aircraft Type': ['d', 2], 'Aircraft Registration': ['f', 2], 
        'Block Fuel': ['seven', 'twenty']})
    with pytest.raises(TypeError):
        csv.converting_dtypes(df)

