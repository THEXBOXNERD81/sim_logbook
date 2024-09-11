# venv Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
# venv .venv\Scripts\activate

import logging
import pandas as pd
import pytest 
from DateTime import DateTime

# ladda in csv data

def load_csv(file_name: str) -> pd.DataFrame:
    # Read the CSV file into a DataFrame and get the wanted columns
    # Needs a try, except
    df = pd.read_csv(file_name)

    column_names = df.columns.values.tolist()

    wanted_columns = ['Aircraft Name', 'Aircraft Type', 'Aircraft Registration', 
                    'Block Fuel', 'Trip Fuel', 'Used Fuel', 
                    'Gross Weight', 'Distance', 'Distance Flown', 
                    'Departure Ident', 'Departure Runway', 'Departure Alt', 
                    'Departure Time', 'Departure Time Sim', 'Destination Ident', 
                    'Destination Runway', 'Destination Alt', 'Destination Time', 
                    'Destination Time Sim']

    for name in column_names:
        if name in wanted_columns:
            pass
        else:
            df = df.drop(name, axis=1)

    return df

def converting_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    # Converting the values of the columns into the wanted data types

    wanted_convertions = {'Aircraft Name': str, 'Aircraft Type': str, 'Aircraft Registration': str, 
                          'Block Fuel': float, 'Trip Fuel': float, 'Used Fuel': float, 
                          'Gross Weight': float, 'Distance': float,  'Distance Flown': float, 
                          'Departure Ident': str, 'Departure Runway': int, 'Departure Alt': int, 
                          'Departure Time': 'datetime64[ns]', 'Departure Time Sim': 'datetime64[ns]', 'Destination Ident': str, 
                          'Destination Runway': int, 'Destination Alt': int, 'Destination Time': 'datetime64[ns]', 
                          'Destination Time Sim': 'datetime64[ns]'}
    


    def convertion(column, type):
        try:
            df[column] = df[column].astype(type)
        except ValueError:
            print()

    departure_and_destination = ['Departure Time', 'Departure Time Sim', 'Destination Time', 'Destination Time Sim']

    for key, value in wanted_convertions.items():
        if key in departure_and_destination:
            # Spliting the datetime value into the correct format for the data type conversion

            df['date'] = df[key].str.split('T').str[0]
            df['time'] = df[key].str.split('T').str[1].str.split('.').str[0]
            df[key] = df['date'] + ' ' + df['time']
            df = df.drop(['date', 'time'], axis=1)

            convertion(key, value)
        else:
            convertion(key, value)


    return df