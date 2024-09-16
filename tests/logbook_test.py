import pytest
import pandas as pd
from unittest.mock import MagicMock

from modules import csv_loading_and_cleaning as csv
import logbook as log


def test_logbook_matching_ids():
    sql_table = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '2023-01-01']]
    df = pd.DataFrame({'Departure Time': ['2023-01-01'], 'Other Column': [1]})
    cursor = MagicMock()
    name = 'test'

    log.logbook(sql_table, df, cursor, name)
    # Add assertions to verify the expected behavior

def test_logbook_sql_larger():
    sql_table = [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '2023-01-01'), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '2023-01-0')]
    df = pd.DataFrame({'Departure Time': ['2023-01-01']})
    cursor = MagicMock()
    name = 'test'

    with pytest.raises(Exception):
        log.logbook(sql_table, df, cursor, name)

def test_logbook_df_larger():
    df = csv.load_logbook('csv_files/Test3.csv')
    df = csv.converting_dtypes(df)
    sql_table = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, df.loc[0, 'Departure Time']]]
    cursor = MagicMock()
    name = 'test'

    log.logbook(sql_table, df, cursor, name)
    # Add assertions to verify the expected behavior

def test_logbook_empty_sql():
    sql_table = []
    df = csv.load_logbook('csv_files/Test3.csv')
    df = csv.converting_dtypes(df)
    cursor = MagicMock()
    name = 'test'

    log.logbook(sql_table, df, cursor, name)
    # Add assertions to verify the expected behavior

def test_logbook_mismatched_ids():
    sql_table = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '2023-01-01']]
    df = pd.DataFrame({'Departure Time': ['2023-01-02'], 'Other Column': [1]})
    cursor = MagicMock()
    name = 'test'

    with pytest.raises(ReferenceError):
        log.logbook(sql_table, df, cursor, name)
