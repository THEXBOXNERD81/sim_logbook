# venv Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
# venv .venv\Scripts\activate

import logging
import sqlalchemy
import pandas as pd
import pytest 
import DateTime

# ladda in csv data

# Read the CSV file into a DataFrame and get the wanted columns
def load_csv(file_name: str) -> pd.DataFrame:
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



df = load_csv('test.csv')

def converting_dtypes(df: pd.DataFrame) -> pd.DataFrame:

    wanted_convertions = {'Aircraft Name': str, 'Aircraft Type': str, 'Aircraft Registration': str, 
                          'Block Fuel': float, 'Trip Fuel': float, 'Used Fuel': float, 
                          'Gross Weight': float, 'Distance': float,  'Distance Flown': float, 
                          'Departure Ident': str, 'Departure Runway': int, 'Departure Alt': int, 
                          'Departure Time': DateTime.DateTime, 'Departure Time Sim': DateTime.DateTime, 'Destination Ident': str, 
                          'Destination Runway': int, 'Destination Alt': int, 'Destination Time': DateTime.DateTime, 
                          'Destination Time Sim': DateTime.DateTime}
    for key, value in wanted_convertions.items():
        print(type(key), value)
        #try:
        #    df[key] = df[key].astype(value)
        #except ValueError:
        #    print(ValueError(f'cant convert column into {value}'))

    return df

df = converting_dtypes(df)

#print(df.dtypes)    
# Get needed columns [Aircraft Name: str, Aircraft Type: str, Aircraft Registration: str, Block Fuel: float, Trip Fuel: float, Used Fuel: float, Gross Weight: float, Distance: float,  Distance Flown: float, Departure Ident: str, Departure Runway: int, Departure Alt: int, Departure Time: DateTime, Departure Time Sim: DateTime, Destination Ident: str, Destination Runway: int, Destination Alt: int, Destination Time: DateTime, Destination Time Sim: DateTime]


# bearbeta viktiga värden

# Skicka in i SQL