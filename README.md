# Simulator Logbook

## Description
A brief description of what your project does and why it exists.

The simulator logbooks take your csv file from Little navmaps and puts into a sql database and creates a new logbook table with a name by choice. The project is made to move the logbook from little navmap into a database for storage. 

link to Little navmap: https://albar965.github.io/

## Table of Contents
- Installation
- Usage
- Contributing
- Contact
- Acknowledgements

## Installation
Download the repository as a zip and unzip the repository.

## Usage

To use the simulator logbook you need to fix some things.
First you need to change the server connection into your sql database and make sure that it connects right to the database. This can be done in the sql_connection module in the modules map.
Secondly in the logbook.py file, you need to change the location of the csv file into the correct directory and file name.
Third you need to change the name into the name of your choice.
Last run logbook.py

Example

```    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-ONKVLR4;'
        'DATABASE=logbook;'
        'Trusted_Connection=yes;'
    )
```
DRIVER, SERVER and DATABASE need to be changed to fit you sql-server and a database needs to be created.

``` file_name = 'C:/right_dir/right_file.csv'
name = 'Some_name'
logbook(sql_table, df, cursor, name, file_name)
```
The file_name and name should be changed too fit the function. The function accepts the arguments directly as values
`logbook(sql_table, df, cursor, 'Some_name', 'C:/right_dir/right_file.csv')

the other function arguments should no be changed or left out.

now run 
`python logbook.py
to put the logbook into your sql table

## Contributing
No need for contributions please.

## Contact
Please do not contact me.

## Acknowledgements
Id like to thank Tishan Nehru for helping me look for typing errors.