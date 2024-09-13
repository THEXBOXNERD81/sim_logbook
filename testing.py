import pytest
import pandas as pd

import sql_connection as sql
import csv_loading_and_cleaning as csv

def test_load_logbook(tmp_file):
    df = csv.load_logbook(tmp_file)
    assert df == pd.DataFrame