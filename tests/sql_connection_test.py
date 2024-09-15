import pytest
import pyodbc

import sql_connection as sql
import csv_loading_and_cleaning as csv


@pytest.fixture
def testing_cursor():
    cursor = sql.connection()
    return cursor

def test_no_connection_trusted():
    # Inline comment show what error message when values are wrong
    with pytest.raises(pyodbc.OperationalError):
        #wrong value in Trusted_connection
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};' #pyodbc.InterfaceError
            'SERVER=DESKTOP-ONKVLR4;' #pyodbc.OperationalError
            'DATABASE=logbook;' #pyodbc.InterfaceError
            'Trusted_Connection=ys;' #pyodbc.OperationalError
        )

def test_no_connection_driver():
    # Inline comment show what error message when values are wrong
    with pytest.raises(pyodbc.InterfaceError):
        # wrong value in driver
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Serer};' #pyodbc.InterfaceError
            'SERVER=DESKTOP-ONKVLR4;' #pyodbc.OperationalError
            'DATABASE=logbook;' #pyodbc.InterfaceError
            'Trusted_Connection=yes;' #pyodbc.OperationalError
        )

def test_connection(testing_cursor):
    assert isinstance(testing_cursor, pyodbc.Cursor)

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

