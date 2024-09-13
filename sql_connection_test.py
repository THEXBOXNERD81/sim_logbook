import pytest
import pyodbc

import sql_connection as sql
import csv_loading_and_cleaning as csv

def test_connection():
    assert isinstance(sql.connection(), pyodbc.Cursor)

@pytest.fixture
def testing_cursor():
    cursor = sql.connection()
    return cursor

def test_create_table(testing_cursor):
    table_name = 'test'
    sql.create_table(testing_cursor, table_name)
    table = sql.get_table(testing_cursor, table_name)
    assert table == []
    

def test_get_table(testing_cursor):
    table = sql.get_table(testing_cursor, 'test')
    assert isinstance(table, list)

def test_insert_table(testing_cursor):
    df = csv.load_logbook('Test3.csv')
    df = csv.converting_dtypes(df)
    sql.insert_table(testing_cursor, df, 'test')
    table = sql.get_table(testing_cursor, 'test')

    assert len(table) != 0
    assert isinstance(table, list) 
    testing_cursor.execute("""DROP TABLE logbook_test""")
    testing_cursor.commit()