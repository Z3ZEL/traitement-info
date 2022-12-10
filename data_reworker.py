import pandas as pd

class Reworker:
    def __init__(self, df):
        self.df = df

    def rework(self):
        df = self.df
        df = df.drop(['ID ','name ','category ','state ','usd pledged ','Unnamed: 13','Unnamed: 14', 'Unnamed: 15','Unnamed: 16'], axis=1)

        #Erase all rows with NaN values
        df = df.dropna()

        #Erase all rows with wrong date format
        df = df[df['deadline '].str.contains("-")]

        #Convert "deadline " and "launched " columns date into timestamp 
        df['deadline '] = pd.to_datetime(df['deadline '])
        df['launched '] = pd.to_datetime(df['launched '])
        df['deadline '] = df['deadline '] - df['launched ']
        df['deadline '] = df['deadline '].dt.total_seconds()


        df_reworked= df[['goal ','pledged ','backers ','country ','currency ','main_category ']]
        #Add new column for duration        
        df_reworked.loc[:,'duration '] = df['deadline ']
        #Clean all none numeric values

        df_reworked = df_reworked[df_reworked['goal '].str.isnumeric()]
        df_reworked = df_reworked[df_reworked['pledged '].str.isnumeric()]
        df_reworked = df_reworked[df_reworked['backers '].str.isnumeric()]
        #map all countries to numeric values
        df_reworked = df_reworked[df_reworked['country '].str.isalpha()]
        df_reworked['country '] = df_reworked['country '].map({'US': 1, 'GB': 2, 'CA': 3, 'AU': 4, 'DE': 5, 'FR': 6, 'NL': 7, 'IT': 8, 'ES': 9, 'SE': 10, 'MX': 11, 'NZ': 12, 'DK': 13, 'IE': 14, 'CH': 15, 'NO': 16, 'BE': 17, 'AT': 18, 'HK': 19, 'SG': 20, 'LU': 21, 'JP': 22})
        df_reworked['country '] = df_reworked['country '].fillna(0)
        #map all currency to numeric values
        df_reworked['currency '] = df_reworked['currency '].map({'USD': 1, 'GBP': 2, 'CAD': 3, 'AUD': 4, 'EUR': 5, 'SEK': 6, 'MXN': 7, 'NZD': 8, 'DKK': 9, 'NOK': 10, 'CHF': 11, 'HKD': 12, 'SGD': 13, 'JPY': 14})
        df_reworked['currency '] = df_reworked['currency '].fillna(0)

        #map all main categories with well optimized values
        df_reworked['main_category '] = df_reworked['main_category '].map({'Film & Video': 1, 'Music': 2, 'Publishing': 3, 'Games': 4, 'Technology': 5, 'Design': 6, 'Art': 7, 'Food': 8, 'Fashion': 9, 'Theater': 10, 'Comics': 11, 'Photography': 12, 'Crafts': 13, 'Journalism': 14, 'Dance': 15})
        #map to 16 for others
        df_reworked['main_category '] = df_reworked['main_category '].fillna(0)
        return df_reworked
