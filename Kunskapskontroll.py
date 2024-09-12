import pyodbc
import pandas
import sql_connection as sql
import csv_loading_and_cleaning as csv

# Check that the csv file and sql table match so we can make sure that the logbooks are the same
def logbook(sql_table: list, df: pandas.DataFrame, cursor: pyodbc.Cursor, name: str):
    """A function that checks if the right logbook is given and updates the logbook with the new entries"""
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
df = csv.load_csv('Test3.csv')

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


