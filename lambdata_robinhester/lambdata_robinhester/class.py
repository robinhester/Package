import pandas
from pandas import DataFrame

class YouTube():
    '''
    Creating a new class based off of the Youtube Dataframe
    used for predictive modeling
    '''
    def __init__(self, name, videoviews, channeltype, country, usercreated, dicto):
        self.name = name
        self.videoviews = videoviews
        self.channeltype = channeltype
        self.country = country
        self.usercreated = usercreated
        self.dicto = dicto

    def name(self):
        print(self.name)

    def videoviews(self):
        print(self.videoviews)

    def channeltype(self):
        print(self.channeltype)

    def country(self):
        print(self.country)

    def usercreated(self):
        print(self.usercreated)

    def create_my_df(self):
        my_df = pandas.DataFrame({'name' : [self.name]},
                                {'videoviews' : [self.videoviews]},
                                {'channeltype' : [self.channeltype]},
                                {'country' : [self.country]},
                                {'usercreated' : [self.usercreated]}
                                )

    def create_my_dict(self):
        my_dict = {self.country : self.dicto}


    def dictionary_feature(my_df, my_dict):
        """
        Adds new column for country name abbreviations
        with full name of country using the map function
        in a column named full name country

        Params: a pandas.DataFrame with a column
        called country and a dictionary

        Example: df = DataFrame({'country': ['US', 'BR', 'IN',
                                             'GB', 'MX']})

                names_map = {'US': 'United States', 'BR': 'Britian',
                 'IN': 'India', 'GB': 'Great Britian',
                 'MX': 'Mexico'}

        Returns: a new pandas.DataFrame column with the full name
        of the country as it's content
        """ 
        my_df['full_name_country']=my_df['country'].map(my_dict)


class Youtube_Wrangling(pandas.DataFrame):
    '''
    Creating a new class based off the Youtube data
    used for predictive modeling, but inheriting 
    the features of the Dataframe class from Pandas module

    Documentation pandas.DataFrame: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

    Params: a youtube based database with the following columns at mininmum:
            name, videoviews, channeltype, usercreated, country 
    '''
    def inspect_head(self):
        print(self.head())

    def dictionary_feature(self, my_dict):
        """
        Adds new column for country name abbreviations
        with full name of country using the map function
        in a column named full name country

        Params: a pandas.DataFrame with a column
        called country and a dictionary

        Example: df = DataFrame({'country': ['US', 'BR', 'IN',
                                             'GB', 'MX']})

                names_map = {'US': 'United States', 'BR': 'Britian',
                 'IN': 'India', 'GB': 'Great Britian',
                 'MX': 'Mexico'}

        Returns: a new pandas.DataFrame column with the full name
        of the country as it's content
        """ 
        self['full_name_country']=self['country'].map(my_dict)

    def name(self):
        print(self.name)

    def videoviews(self):
        print(self.videoviews)

    def channeltype(self):
        print(self.channeltype)

    def usercreated(self):
        print(self.usercreated)

    def country(self):
        print(self.country)

    def inspect_columns(self):
        print(self.df.columns)

if __name__ == "__main__":

    youtuber = YouTube('Pewdiepie','20,000','Entertainment','US','10/10/2003','United States')

    youtuber.name
    youtuber.videoviews
    youtuber.channeltype
    youtuber.country
    youtuber.usercreated
    df=youtuber.create_my_df()
    print(df)
    dictionary=youtuber.create_my_dict()
    print(dictionary)
    df=df.dictionary_feature()
    print(df)

    pass
