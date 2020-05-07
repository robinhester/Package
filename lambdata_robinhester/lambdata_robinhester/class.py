class YouTube(object):
    '''
    Creating a new class based off of the Youtube Dataframe
    used for predictive modeling
    '''
    def__init__(self, my_df)
        self.my_df = my_df

    def name(self):
        print(self.my_df.name)

    def videoviews(self):
        print(self.my_df.videoviews)

    def channeltype(self):
        print(self.my_df.channeltype)

    def country(self):
        print(self.my_df.country)

    def usercreated(self):
        print(self.my_df.usercreated)

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
        self.my_df['full_name_country']=self.my_df['country'].map(my_dict)


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
