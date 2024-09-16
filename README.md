# Simulator Logbook

## Description
A brief description of what your project does and why it exists.

The Simulator Logbook takes your CSV file from Little Navmap and imports it into an SQL database, creating a new logbook table with a name of your choice. This project is designed to move the logbook from Little Navmap into a database for better storage and management.
 

link to Little navmap: https://albar965.github.io/

## Table of Contents
- Installation
- Usage
- Contributing
- Contact
- Acknowledgements

## Installation
Download the repository as a zip and unzip the repository.
packages needed for this program are

-pandas

-pyocdb

## Usage

To use the Simulator Logbook, follow these steps:
1. Change the server connection in the `sql_connection` module to your SQL database. Ensure it connects correctly.
2. In the `logbook.py` file, update the location of the CSV file to the correct directory and file name.
3. Change the name to your desired logbook name.
4. Run `logbook.py`.

Example:
```python
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=YOUR_SERVER;'
    'DATABASE=YOUR_DATABASE;'
    'Trusted_Connection=yes;'
)
```
Update DRIVER, SERVER, and DATABASE to match your SQL server configuration.

``` file_name = 'C:/your_directory/your_file.csv'
name = 'Your_Logbook_Name'
logbook(sql_table, df, cursor, name, file_name)
```
Ensure file_name and name are updated to fit your setup. The function accepts these arguments directly as values:
`logbook(sql_table, df, cursor, 'Your_Logbook_Name', 'C:/your_directory/your_file.csv')

the other function arguments should no be changed or left out.

Finally, run: 
`python logbook.py
to import the logbook into your SQL table.

## Contributing
Contributions does not need to be made since i wont be improving or updating the project.

## Acknowledgements
Id like to thank Tishan Nehru for helping me look for typing errors.