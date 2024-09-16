import pytest
import pyodbc

from modules import sql_connection as sql
from modules import csv_loading_and_cleaning as csv


@pytest.fixture
# A cursor is made to avoid redundancy
def testing_cursor():
    cursor = sql.connection()
    return cursor

def test_no_connection_trusted():
    # This test checkes that it raises a pyodbc.OperationalError when a typo is made in one of the values is made
    # Inline comment show what error message when values are wrong
    with pytest.raises(pyodbc.OperationalError):
        #Wrong value in Trusted_connection
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};' #pyodbc.InterfaceError
            'SERVER=DESKTOP-ONKVLR4;' #pyodbc.OperationalError
            'DATABASE=logbook;' #pyodbc.InterfaceError
            'Trusted_Connection=ys;' #pyodbc.OperationalError
        )

def test_no_connection_driver():
    # This test checkes that it raises a pyodbc.OperationalError when a typo is made in one of the values is made
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
    # Test to check that a connection is made by returning the correct datatype
    assert isinstance(testing_cursor, pyodbc.Cursor)

def test_create_table(testing_cursor):
    # Test that checks if a table was created by retrieving the table and checking that the table is empty  
    table_name = 'test'
    sql.create_table(testing_cursor, table_name)
    table = sql.get_table(testing_cursor, table_name)
    assert table == []
    

def test_get_table(testing_cursor):
    # Test that a table can be retrived by checking that the table is a list
    table = sql.get_table(testing_cursor, 'test')
    assert isinstance(table, list)

def test_wrong_table(testing_cursor):
    # test that checks for pyodbc.ProgrammingError by searching for a non existing table
    with pytest.raises(pyodbc.ProgrammingError):
        table = sql.get_table(testing_cursor, 'wrong table')


def test_insert_table(testing_cursor):
    # Test that tries to insert a dataframe into a sql table and checking if the table is not 0 and that it is a list
    df = csv.load_logbook('csv_files/Test3.csv')
    df = csv.converting_dtypes(df)
    sql.insert_table(testing_cursor, df, 'test')
    table = sql.get_table(testing_cursor, 'test')

    assert len(table) != 0
    assert isinstance(table, list) 

    #this is done to remove the test table for future tests
    testing_cursor.execute("""DROP TABLE logbook_test""")
    testing_cursor.commit()

