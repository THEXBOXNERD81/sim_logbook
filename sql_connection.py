import sqlalchemy
import pytest
import logging
import pyodbc
import pandas as pd

def connection() -> pyodbc.Cursor:
    #Connecting to sql database logbook
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-ONKVLR4;'
        'DATABASE=logbook;'
        'Trusted_Connection=yes;'
    )

    cursor = conn.cursor()
    print('connected to server')

    return cursor


def create_table(cursor: pyodbc.Cursor, name: str):
    # Creating a table in the sql database with given name
    cursor.execute(f""" 
                   CREATE TABLE logbook_{name} (
                        Aircraft_Name VARCHAR(8000), Aircraft_Type VARCHAR(8000), Aircraft_Registration VARCHAR(8000), 
                        Block_Fuel FLOAT, Trip_Fuel FLOAT, Used_Fuel FLOAT, 
                        Gross_Weight FLOAT, Distance FLOAT, Distance_Flown FLOAT,
                        Departure_Ident VARCHAR(8000), Departure_Runway INT, Departure_Alt INT, 
                        Departure_Time DATETIME, Departure_Time_Sim DATETIME, Destination_Ident VARCHAR(8000), 
                        Destination_Runway INT, Destination_Alt INT, Destination_Time DATETIME, Destination_Time_Sim DATETIME
                    )
        """)
    
    cursor.commit()
    return print('Table Created')



def get_table(cursor: pyodbc.Cursor):
    pass



def insert_table(cursor: pyodbc.Cursor, df: pd.DataFrame, name: str):
    # Insertinng the values from the csv file
    for row in df.itertuples():
        cursor.execute(f"""
            INSERT INTO logbook.dbo.logbook_{name} (
                Aircraft_Name, Aircraft_Type, Aircraft_Registration, 
                Block_Fuel, Trip_Fuel, Used_Fuel, 
                Gross_Weight, Distance, Distance_Flown,
                Departure_Ident, Departure_Runway, Departure_Alt, 
                Departure_Time, Departure_Time_Sim, Destination_Ident, 
                Destination_Runway, Destination_Alt, Destination_Time, Destination_Time_Sim
            )
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,

            # row._n is replacing the column names with spaces in them. this happens when using df.itertuples()
            # row._1 == row.Aircraft_name and so on
        
            row._1, row._2, row._3, 
            row._4, row._5, row._6, 
            row._7, row.Distance, row._9,
            row._10, row._11, row._12, 
            row._13, row._14, row._15, 
            row._16, row._17, row._18, 
            row._19
            )
        cursor.commit()
        return print('Values inserted into given Table')
    


    