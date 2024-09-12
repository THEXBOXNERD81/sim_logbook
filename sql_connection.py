import logging
import pyodbc
import pandas as pd

def connection() -> pyodbc.Cursor:
    """
    Establishes a connection to the SQL Database 'logbook' and returns a cursor object.

    Returns:
    pyodbc.Cursor: A cursor object to interact with the SQL Database.

    The function connects to the SQL Server using the ODBC Driver 17 for SQL Server,
    targeting the 'logbook' database on the specified server. It uses a trusted connection
    for authentication. Upon successful connection, it returns a cursor object for executing
    SQL queries.

    Connection details:
    - DRIVER: ODBC Driver 17 for SQL Server
    - SERVER: DESKTOP-ONKVLR4
    - DATABASE: logbook
    - Trusted_Connection: yes

    Example usage:
    cursor = connection()
    """
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


def create_table(cursor: pyodbc.Cursor, name: str) -> None:
    """
    Creates a SQL table for the logbook database with the specified name.

    Parameters:
    cursor (pyodbc.Cursor): The cursor object to execute SQL commands.
    name (str): The name to be appended to the logbook table.

    Returns:
    None

    The function constructs and executes a SQL command to create a new table in the logbook database.
    The table includes columns for various logbook attributes such as aircraft details, fuel usage,
    weights, distances, and departure and destination information. After creating the table, the function
    commits the transaction and prints a confirmation message.

    Table columns:
    - Aircraft_Name: VARCHAR(8000)
    - Aircraft_Type: VARCHAR(8000)
    - Aircraft_Registration: VARCHAR(8000)
    - Block_Fuel: FLOAT
    - Trip_Fuel: FLOAT
    - Used_Fuel: FLOAT
    - Gross_Weight: FLOAT
    - Distance: FLOAT
    - Distance_Flown: FLOAT
    - Departure_Ident: VARCHAR(8000)
    - Departure_Runway: INT
    - Departure_Alt: INT
    - Departure_Time: DATETIME
    - Departure_Time_Sim: DATETIME
    - Destination_Ident: VARCHAR(8000)
    - Destination_Runway: INT
    - Destination_Alt: INT
    - Destination_Time: DATETIME
    - Destination_Time_Sim: DATETIME

    Example usage:
    create_table(cursor, 'example_name')
    """
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



def get_table(cursor: pyodbc.Cursor, name: str) -> list:
    """
    Retrieves all rows and columns from the specified SQL table in the logbook database.

    Parameters:
    cursor (pyodbc.Cursor): The cursor object to execute SQL commands.
    name (str): The name of the table to retrieve.

    Returns:
    list: A list of tuples representing the rows in the SQL table.

    The function constructs and executes a SQL query to select all columns and rows from the specified
    table in the logbook database. It fetches all the results and returns them as a list of tuples.

    Example usage:
    sql_table = get_table(cursor, 'example_name')
    """
    # A function that fetches the table of the logbook 
    cursor.execute(f"""
        SELECT * FROM logbook_{name}
    """)

    sql_table = cursor.fetchall()

    return sql_table



def insert_table(cursor: pyodbc.Cursor, df: pd.DataFrame, name: str) -> None:
    """
    Inserts the DataFrame values into the specified SQL table in the logbook database.

    Parameters:
    cursor (pyodbc.Cursor): The cursor object to execute SQL commands.
    df (pd.DataFrame): The DataFrame containing the data to be inserted.
    name (str): The name to be appended to the logbook table.

    Returns:
    None

    The function iterates over the rows of the DataFrame and inserts each row into the specified
    table in the logbook database. It uses parameterized queries to safely insert the data,
    and commits the transaction after all rows have been inserted.

    Example usage:
    insert_table(cursor, df, 'example_name')
    """
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
        
            row._1, row._2, row._3,             # row._n is replacing the column names with spaces in them
            row._4, row._5, row._6,             # row._1 == row.Aircraft_name and so on
            row._7, row.Distance, row._9,
            row._10, row._11, row._12, 
            row._13, row._14, row._15, 
            row._16, row._17, row._18, 
            row._19
            )
    cursor.commit()
    return print('Values inserted into given Table')
    


    