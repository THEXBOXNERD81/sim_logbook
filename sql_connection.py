import sqlalchemy
import pytest
import logging
import pyodbc
import pandas as pd

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


def create_table(cursor: pyodbc.Cursor, name: str):
    # Creating a table in the sql database with given name
    cursor.execute(f""" 
                   CREATE TABLE Logbook.{name} (
                        Aircraft_Name VARCHAR, Aircraft_Type VARCHAR, Aircraft_Registration VARCHAR, 
                        Block_Fuel FLOAT, Trip_Fuel FLOAT, Used_Fuel FLOAT, 
                        Gross_Weight FLOAT, Distance FLOAT, Distance_Flown FLOAT,
                        Departure_Ident VARCHAR, Departure_Runway INT, Departure_Alt INT, 
                        Departure_Time TIMESTAMP, Departure_Time_Sim TIMESTAMP, Destination_Ident VARCHAR, 
                        Destination_Runway INT, Destination_Alt INT, Destination_Time TIMESTAMP, Destination_Time_Sim TIMESTAMP
                    )
        """)
    
    return 'Table Created'



def get_table(cursor: pyodbc.Cursor):
    pass



def insert_table(cursor: pyodbc.Cursor, df: pd.DataFrame, name: str):
    # Insertinng the values from the csv file
    for row in df.itertuples():
        cursor.execute(f"""
            INSERT INTO logbook.dbo.logbook.{name} (
                Aircraft_Name, Aircraft_Type, Aircraft_Registration, 
                Block_Fuel, Trip_Fuel, Used_Fuel, 
                Gross_Weight, Distance, Distance_Flown,
                Departure_Ident, Departure_Runway, Departure_Alt, 
                Departure_Time, Departure_Time_Sim, Destination_Ident, 
                Destination_Runway, Destination_Alt, Destination_Time, Destination_Time_Sim
            )
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            row.Aircraft_Name, row.Aircraft_Type, row.Aircraft_Registration, 
            row.Block_Fuel, row.Trip_Fuel, row.Used_Fuel, 
            row.Gross_Weight, row.Distance, row.Distance_Flown,
            row.Departure_Ident, row.Departure_Runway, row.Departure_Alt, 
            row.Departure_Time, row.Departure_Time_Sim, row.Destination_Ident, 
            row.Destination_Runway, row.Destination_Alt, row.Destination_Time, row.Destination_Time_Sim
        )

        return 'Values inserted into given Table'
    


    