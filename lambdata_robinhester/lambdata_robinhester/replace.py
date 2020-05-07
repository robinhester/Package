# create a function that allows you to add
# a dictionary and add a column with new dict
# values
# FL ---> Florida
# ATL --> Atlanta
import pandas
from pandas import DataFrame


def dictionary_feature(my_df, my_dict):
    """
    Allows you to pass in a dataframe and
    a dictionary that returns a new dataframe
    with the abbreviations returned with full names
    in a new column, using the map function

    Params: my_df a pandas.DataFrame with a column
    called abbrev and a dictionary

    Example: df = DataFrame({'abbrev': ['CA', 'CO', 'CT',
                               'DC', 'TX']})

            names_map = {'CA': 'California', 'CO': 'Colorado',
                 'CT': 'Conneticut', 'DC': 'District of Columbia',
                 'TX': 'Texas'}

    Returns: a new pandas.DataFrame with the original
    col as well as a 'full_name' column
    """
    # Abbreviation to Full Name
    # makes a copy of the original dataframe passed

    new_df = my_df.copy()

    # uses the map feature to apply the dictionary
    # and return a new column with the full names

    new_df['full_name'] = new_df['abbrev'].map(my_dict)

    return new_df

if __name__ == "__main__":

    names_map = {'CA': 'California', 'CO': 'Colorado',
                 'CT': 'Conneticut', 'DC': 'District of Columbia',
                 'TX': 'Texas'}

    city_names_map = {'ATL': 'Atlanta',
                      'KS Cty': 'Kansas City',
                      'ST. Louis': 'Saint Louis',
                      'NYC': 'New York City',
                      'L.A.': 'Los Angeles'}

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT',
                               'DC', 'TX']})

    df2 = DataFrame({'abbrev': ['ATL', 'KS Cty',
                                'ST. Louis', 'NYC', 'L.A.']})

    print(dictionary_feature(df, names_map))

    print(dictionary_feature(df2, city_names_map))

    pass
