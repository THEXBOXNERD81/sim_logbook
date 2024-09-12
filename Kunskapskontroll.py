import pyodbc
import pandas
import sql_connection as sql
import csv_loading_and_cleaning as csv

# Check that the csv file and sql table match so we can make sure that the logbooks are the same
def logbook(sql_table: list, df: pandas.DataFrame, cursor: pyodbc.Cursor, name: str):
    """
    Checks if the provided logbook matches the SQL table and updates the logbook with new entries.

    Parameters:
    sql_table (list): The SQL table data as a list of rows.
    df (pandas.DataFrame): The DataFrame containing the new logbook entries.
    cursor (pyodbc.Cursor): The database cursor for executing SQL commands.
    name (str): The name of the SQL table to update.

    Raises:
    FileNotFoundError: If the CSV logbook does not match the SQL table.
    Exception: If the SQL table is larger than the CSV file, indicating an old CSV file or duplicate values in the SQL database.

    Notes:
    - The function first checks if the logbook IDs match between the SQL table and the DataFrame.
    - If the IDs match and the lengths are equal, it exits without updating.
    - If the SQL table is larger, it raises an exception.
    - If the DataFrame is larger, it updates the SQL table with the new entries.
    - If the SQL table is empty, it inserts all entries from the DataFrame.

    Example:
    logbook(sql_table, df, cursor, 'logbook_name')
    """
    try: 
        #this is done to get a form of id to make sure that the same logbooks are being used
        #If there is no values in the table, then there shouldn't be an error occuring
        sql_date_id = sql_table[0][12]
        df_date_id = df['Departure Time'][0]
    except:
        print('No values in SQL table')
        sql_date_id = 1
        df_date_id = 0

    sql_length = len(sql_table)
    df_length = len(df)
    
    if sql_date_id == df_date_id:
        print('csv files macth')
        if len(sql_table) == len(df):
            print('Nothing to update')
            quit()
        elif len(sql_table) > len(df):
            raise print('SQL Table larger than csv. Old csv file used or duplicate values in SQL database')
        else:
            df = df[:][sql_length:df_length]
            sql.insert_table(cursor, df, name)
            
    elif sql_table == []:
        df = df[:][sql_length:df_length]
        sql.insert_table(cursor, df, name)

    else:
        raise FileNotFoundError('The csv logbook does not match the sql table, use the same logbook as used in the sql database')

# Load logbook csv and convert the datatypes to integrate into the SQL Database
#T:E: log INFO, critical
df = csv.load_logbook('Test3.csv')

# T:E log INFO, Critical
df = csv.converting_dtypes(df)

# Make the connection to the SQL Server
#T:E INFO, Critical
cursor = sql.connection()

# Make a new table for the user else just insert the csv data
name = 'leonardo'

try:
    # A New table should be created only if there isn't a table for the given name, then the already created logbook should be used
    sql.create_table(cursor, name)
except pyodbc.ProgrammingError:
    # log INFO
    print('There is already a table named that in the database.')


sql_table = sql.get_table(cursor, name)

logbook(sql_table, df, cursor, name)


