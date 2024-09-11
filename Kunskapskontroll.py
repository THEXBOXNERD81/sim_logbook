import pyodbc

import sql_connection as sql
import csv_loading_and_cleaning as csv

# Load in the logbook csv file to integrate into the SQL Database
df = csv.load_csv('test.csv')

# Convert the datatypes to the correct types for the SQL integration
df = csv.converting_dtypes(df)

# Make the connection to the SQL Server
cursor = sql.connection()

# Make a new table for the user else just insert the csv data
try:
    sql.create_table(cursor, 'leonardo')
except pyodbc.ProgrammingError:
    print('There is already a table named that in the database.')


sql_table = sql.get_table(cursor, 'leonardo')
sql_date_id = sql_table[0][12]
df_date_id = df['Departure Time'][0]

if sql_date_id == df_date_id:
    print('csv files macth')
    sql.insert_table(cursor, df, 'leonardo')

elif sql_table == []:
    sql.insert_table(cursor, df, 'leonardo')

else:
    raise ReferenceError('The csv logbook does not match the sql table, use the same logbook as used in the sql database')



