import sql_connection as sql
import csv_loading_and_cleaning as csv

df = csv.load_csv('test.csv')

df = csv.converting_dtypes(df)

cursor = sql.connection()

sql.create_table(cursor, 'leonardo')

sql.insert_table(cursor, df, 'leonardo')