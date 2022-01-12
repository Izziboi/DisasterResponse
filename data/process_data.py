# Import libraries

import sys
import pandas as pd
from pandas import Series
import sqlite3
from sqlalchemy import create_engine

# Dataset and database file paths
disaster_messages = 'data/disaster_messages.csv'
disaster_categories = 'data/disaster_categories.csv'
DisasterResponse = 'sqlite:///data/DisasterResponse.db'

class ETLPipline:
    '''
    This class is the ETL pipeline class. It takes the messages and categories datasets, tydies them up, merges them and loads 
    them into a SQLite file.
    
    INPUT:
    1. messages_filepath: A file path leading to the location of the messages dataset in csv format.
    2. categories_filepath: A file path leading to the location of the categories dataset in csv format.
    3. database_filepath: A database file path with a database file name of choice. This database would be created as a SQLite 
    file when the program is run, and saved in the directory the path is pointing to.
    
    OUTPUT:
    SQLite (.db) file: database_filename created with the merged dataset inserted in it as a table and saved in the directory 
    where the given path points to.
    '''
    
    def __init__(self, messages_filepath, categories_filepath, database_filepath):
        
        # Instantiate the arguments
        self.messages_filepath = messages_filepath
        self.categories_filepath = categories_filepath
        self.database_filepath = database_filepath
              

    def load_data(self):
        '''
        This method loads the messages and categories datasets by imbibing the messages_filepath and categories_filepath from 
        the class. It also merges both of them
        
        INPUT:
        1. The messages_filepath of the class.
        2. The categories_filepath of the class.
        
        OUTPUT:
        Dataframe: A dataset of the merged two datasets in a dataframe format.
        '''
        messages = pd.read_csv(self.messages_filepath) # Load the messages dataset
        
        categories = pd.read_csv(self.categories_filepath) # Load the categories dataset
        
        d_f = messages.merge(categories, how='outer', on=['id']) # Merge the original datasets
        return d_f
          
    
    def clean_data(self, df):
        '''
        This method cleans the two datasets. It sets each category as a column and creates numerical variables for them. It
        then concatenates the two datasets and saves it as a SQLite database file.
        
        INPUT:
        1. df: A dataframe of the original datasets simply merged together, using id as the common key. This is the output of
        the load_data() method.
        
        OUTPUT:
        DAtaframe: A dataset of the cleaned, concatenated datasets.
        '''
        
        categories = df['categories'].str.split(';', expand=True) # Split the categories
        
        row = categories.loc[0] # Select the first row of the categories dataframe
        
        category_colnames = row.replace('-.+', '', regex=True) # Extract a list of new column names for categories.
        
        categories.columns = category_colnames # Rename the columns of 'categories'
        
        # Convert category values to just numbers 0 or 1
        for column in categories:
            categories[column] = categories[column].str.split('-').str.get(1)
            categories[column] = pd.to_numeric(categories[column])
            categories.head()
        
        df.drop(['original'], axis=1, inplace=True) # Drop the 'original' column
        
        df = pd.concat([df, categories], axis=1) # Concatenate the new categories dataframe with the merged dataset
        
        duplicate_df = df[df.duplicated()] # Check for duplicates
        
        df = df.drop_duplicates() # Remove duplicates

        return df
    
    def save_data(self, dframe):
        '''
        This method takes the cleaned dataset and saves it as a SQLite file to a location in the directory path provided by the 
        user. It already imbibes the database_filepath of the class. The user should also provide a table name of choice inside
        the code, at the return statement.
        
        INPUT:
        1. dframe: The cleaned, concatenated dataset. This is the output of the clean_data() method.
        2. table_name: str: Any suitable table name; must be wrapped in quotation signs, e.g. 'mytable'.
        
        OUTPUT:
        SQLite (.db) file: database_filename created with the merged dataset inserted in it as a table and saved in the 
        directory where the given path points to.
        '''
        engine = create_engine(self.database_filepath)
        return dframe.to_sql('dtable', engine, index=False, if_exists='replace')
    
etl = ETLPipline(disaster_messages, disaster_categories, DisasterResponse) # Instance of the class


def main():
        if len(sys.argv) == 4:

            disaster_messages, disaster_categories, DisasterResponse = sys.argv[1:]

            print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
                  .format(disaster_messages, disaster_categories))
            df = etl.load_data()

            print('Cleaning data...')
            df = etl.clean_data(df)

            print('Saving data...\n    DATABASE: {}'.format(df))
            etl.save_data(df)

            print('Cleaned data saved to database!')
    
        else:
            print('Please provide the filepaths of the messages and categories '\
                  'datasets as the first and second argument respectively, as '\
                  'well as the filepath of the database to save the cleaned data '\
                  'to as the third argument. \n\nExample: python process_data.py '\
                  'disaster_messages.csv disaster_categories.csv '\
                  'DisasterResponse.db')

if __name__ == '__main__':
    main()
