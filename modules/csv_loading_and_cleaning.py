import pandas as pd

def load_logbook(file_name: str) -> pd.DataFrame:
    """
    Loads a given logbook CSV file and returns a DataFrame with the specified columns.

    Parameters:
    file_name (str): The name of the CSV file to be loaded.

    Returns:
    pd.DataFrame: A DataFrame containing only the specified columns for a logbook.

    The function reads the CSV file into a DataFrame, then filters out any columns
    that are not in the list of wanted columns. The resulting DataFrame contains
    only the columns relevant to the logbook.

    Wanted columns:
    - 'Aircraft Name'
    - 'Aircraft Type'
    - 'Aircraft Registration'
    - 'Block Fuel'
    - 'Trip Fuel'
    - 'Used Fuel'
    - 'Gross Weight'
    - 'Distance'
    - 'Distance Flown'
    - 'Departure Ident'
    - 'Departure Runway'
    - 'Departure Alt'
    - 'Departure Time'
    - 'Departure Time Sim'
    - 'Destination Ident'
    - 'Destination Runway'
    - 'Destination Alt'
    - 'Destination Time'
    - 'Destination Time Sim'
    """

    df = pd.read_csv(file_name)

    wanted_columns = [
        'Aircraft Name', 'Aircraft Type', 'Aircraft Registration', 
        'Block Fuel', 'Trip Fuel', 'Used Fuel', 
        'Gross Weight', 'Distance', 'Distance Flown', 
        'Departure Ident', 'Departure Runway', 'Departure Alt', 
        'Departure Time', 'Departure Time Sim', 'Destination Ident', 
        'Destination Runway', 'Destination Alt', 'Destination Time', 
        'Destination Time Sim'
        ]

    column_names = df.columns.values.tolist()

    for name in column_names:
        if name in wanted_columns:
            pass
        else:
            df = df.drop(name, axis=1)

    return df

def converting_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts data types of columns in the logbook DataFrame to the required data types for an SQL table.

    Parameters:
    df (pd.DataFrame): The DataFrame containing logbook data.

    Returns:
    pd.DataFrame: A DataFrame with columns converted to the specified data types.

    The function iterates over a predefined dictionary of column names and their desired data types,
    converting each column to the appropriate type. Special handling is applied to datetime columns
    to ensure they are in the correct format before conversion.

    Wanted conversions:
    - 'Aircraft Name': str
    - 'Aircraft Type': str
    - 'Aircraft Registration': str
    - 'Block Fuel': float
    - 'Trip Fuel': float
    - 'Used Fuel': float
    - 'Gross Weight': float
    - 'Distance': float
    - 'Distance Flown': float
    - 'Departure Ident': str
    - 'Departure Runway': int
    - 'Departure Alt': int
    - 'Departure Time': 'datetime64[ns]'
    - 'Departure Time Sim': 'datetime64[ns]'
    - 'Destination Ident': str
    - 'Destination Runway': int
    - 'Destination Alt': int
    - 'Destination Time': 'datetime64[ns]'
    - 'Destination Time Sim': 'datetime64[ns]'

    The function also includes a nested function `convertion` that handles the actual conversion
    of each column, with error handling for type conversion issues.
    """
    # Converting the values of the columns into the wanted data types

    wanted_convertions = {
        'Aircraft Name': str, 'Aircraft Type': str, 'Aircraft Registration': str, 
        'Block Fuel': float, 'Trip Fuel': float, 'Used Fuel': float, 
        'Gross Weight': float, 'Distance': float,  'Distance Flown': float, 
        'Departure Ident': str, 'Departure Runway': int, 'Departure Alt': int, 
        'Departure Time': 'datetime64[ns]', 'Departure Time Sim': 'datetime64[ns]', 'Destination Ident': str, 
        'Destination Runway': int, 'Destination Alt': int, 'Destination Time': 'datetime64[ns]', 
        'Destination Time Sim': 'datetime64[ns]'
        }
    


    def convertion(column, type):
        """ 
        A function that converts the datatype from
        the given column into the given datatype.
        """
        try:
            df[column] = df[column].astype(type)
        except ValueError as e:
            raise TypeError(f'{e}') 

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