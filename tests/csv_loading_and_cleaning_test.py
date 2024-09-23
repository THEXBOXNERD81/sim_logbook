import pytest
import pandas as pd

from modules import csv_loading_and_cleaning as csv

@pytest.fixture
# A dataframe is loaded with a test file to avoid redundancy
def testing_df():
    df = csv.load_logbook('csv_files/Test3.csv')
    return df

def test_load_logbook(testing_df):
    # Test that checks that a dataframe is loaded by checking its datatype
    assert isinstance(testing_df, pd.DataFrame)

def test_load_non_existing_file():
    # Test that checks for the FileNotFoundError error when typing a file that doesnt exist
    with pytest.raises(FileNotFoundError):
        csv.load_logbook('csv_files/does_not_exist_file.csv')

def test_load_non_permission_file():
    # Test that checks for the PermissionError error when the function cant get acces to the file
    with pytest.raises(PermissionError):
        csv.load_logbook('C:/Windows/System32')

def test_converting_dtypes(testing_df):
    # Test that checks that data types where converted by checking that no exceptions where raised 
    try:
        csv.converting_dtypes(testing_df)
    except Exception as e:
        pytest.fail(f"Unexpected exception {e}")

def test_converting_dtypes_with_wrong_columns():
    # Test that checks for a KeyError error when wrong columns are listed in the dataframe
    df = pd.DataFrame({'Aircraft Name': ['x', 2], 'Wrong column': ['d', 2], 'Aircraft Registration': ['f', 2], 
        'Block Fuel': ['seven', 'twenty']})
    with pytest.raises(KeyError):
        csv.converting_dtypes(df)

def test_convert_wrong_dtypes():
    # Test that checks for a TypeError error when wrong data types are listed in the dataframe
    df = pd.DataFrame({'Aircraft Name': ['x', 2], 'Aircraft Type': ['d', 2], 'Aircraft Registration': ['f', 2], 
        'Block Fuel': ['seven', 'twenty']})
    with pytest.raises(TypeError):
        csv.converting_dtypes(df)

