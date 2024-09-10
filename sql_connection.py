import sqlalchemy
import pytest
import logging
import pyodbc

def connection():
    #Connecting to sql database logbook
    conn = pyodbc.connect(
        Trusted_Connection = 'Yes',
        Driver = {'ODBC Driver 17 for SQL Server'},
        Server = 'DESKTOP-ONKVLR4',
        database = 'logbook'
    )

    cursor = conn.cursor()

    return cursor
