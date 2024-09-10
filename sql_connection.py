import sqlalchemy
import pytest
import logging
import pyodbc

def connection() -> pyodbc.Cursor:
    #Connecting to sql database logbook
    conn = pyodbc.connect(
        Trusted_Connection = 'Yes',
        Driver = {'ODBC Driver 17 for SQL Server'},
        Server = 'DESKTOP-ONKVLR4',
        database = 'logbook'
    )

    cursor = conn.cursor()

    return cursor


def create_table(cursor: pyodbc.Cursor):
    pass



def get_table(cursor: pyodbc.Cursor):
    pass



def insert_table(cursor: pyodbc.Cursor):
      pass