import pyodbc
import pandas
import logging

from modules import sql_connection as sql
from modules import csv_loading_and_cleaning as csv



logging.basicConfig(
    filename='logbook_logfile.log',
    format='[%(asctime)s][%(levelname)s] %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger()

file_name = 'csv_files/Test3.csv'
name = 'leonardo'

# Check that the csv file and sql table match so we can make sure that the logbooks are the same
def logbook(sql_table: list, df: pandas.DataFrame, cursor: pyodbc.Cursor, name: str, file_name: str) -> None:
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
        # This is done to get a form of id to make sure that the same logbooks are being used
        # If there is no values in the table, then there shouldn't be an error occuring
        sql_date_id = sql_table[0][12]
        df_date_id = df['Departure Time'][0]
    except:
        # This is done to avoid an Exception in the later stages when we need a missmatching id
        sql_date_id = 1
        df_date_id = 0

    sql_length = len(sql_table)
    df_length = len(df)
    
    if sql_date_id == df_date_id:
        logger.info('csv file and the SQL table macth')
        if len(sql_table) == len(df):
            logger.info('Nothing to update')
            return
        elif len(sql_table) > len(df):
            logger.warning('SQL Table larger than csv. Old csv file used or duplicate values in SQL database')
            raise Exception
        else:
            df = df[:][sql_length:df_length]
            sql.insert_table(cursor, df, name)
            logger.info(f'Values where succefully insert into logbook_{name}')
            logger.info('Program is shutting down')
            return
            
    elif sql_table == []:
        df = df[:][sql_length:df_length]
        sql.insert_table(cursor, df, name)
        logger.info(f'Values where succefully insert into logbook_{name}')
        logger.info('Program is shutting down')
        return

    else:
        raise ReferenceError('The csv logbook does not match the sql table, use the same logbook as used in the sql database')

# Load logbook csv and convert the datatypes to integrate into the SQL Database
try:
    df = csv.load_logbook(file_name)
    logger.info('Requested file succesfully loaded')
except FileNotFoundError as e:
    logger.critical('The wanted file could not be loaded')
    logger.debug(e)
    quit()
except PermissionError as e:
    logger.critical('Could not get acces to the wanted file')
    logger.debug(e)
    quit()

try:
    df = csv.converting_dtypes(df)
    logger.info('Values converted to correct data types')
except TypeError as e:
    logger.critical("Couldn't convert the values into the wanted datatypes")
    logger.debug(e)
    quit()

# Make the connection to the SQL Server
try:
    cursor = sql.connection()
    logger.info('Connection to server was made')
except pyodbc.OperationalError as e:
    logger.critical("Connection couldn't be made to the server")
    logger.debug(e)
    quit()
except pyodbc.InterfaceError as e:
    logger.critical("Connection couldn't be made to the server")
    logger.debug(e)
    quit()

# Make a new table for the user else just insert the csv data


try:
    # A New table should be created only if there isn't a table for the given name, then the already created logbook should be used
    sql.create_table(cursor, name)
    logger.info(f'New table was made for {name}')
except pyodbc.ProgrammingError:
    logger.info(f'There is already a table for {name} in the database.')

# Retrieve the SQL table for the given name
try:
    sql_table = sql.get_table(cursor, name)
    logger.info(f'SQL table retrieved from logbook_{name}')
except pyodbc.ProgrammingError as e:
    logger.critical(f"Couldn't retrieve SQL table for logbook_{name}")
    logger.debug(e)
    quit()



logbook(sql_table, df, cursor, name, file_name)