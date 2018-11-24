import json
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups')

class SmartLookup(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return key.title()
        return key


def to_lookup(dict):

    lookup  = SmartLookup()

    for key, values in dict.items():
        for value in values:
            lookup[value] = key


    return lookup

def country_name_filter_apply(name, countries):
    """
    Now assign the country name in different steps : first check if the name to analysed called "name" matches one of the country name (in english) then just return that value. If not, Check that it does not match one of the country label (format cca2 by choice and since it's also in the json for the map so should use this one to compare with the map). Then, if no match yet, check if the "name" is CONTAINED in the alias (set of all country names in different languages and official/non-official). Problem: many returns possible. Check if one of these return has a value of 1 in his forced column, then assign that one. If none is forced or more then one is, don't assign and return the original country name. It would be good in the future to find these instances where none is forced so that we can add them to the list.
   
   countries has the following structure : ['name', 'cca2', 'alias', 'Forced']
   """
    if(name.lower() == "unknown"):
        return "Unknown"
    country_set_name = countries[countries.name.apply(lambda x: x.lower()  == name.lower())]
    if(not country_set_name.empty):
        if(country_set_name.shape[0]==1):
            return country_set_name.iloc[0,0]
      
    country_set_cca2 = countries[countries.cca2.apply(lambda x: str(x).lower()== name.lower())]
    if(not country_set_cca2.empty):
        if(country_set_cca2.shape[0]==1):
            return country_set_cca2.iloc[0,0]
     
    country_set = countries[countries['alias'].str.contains(name, case=False)]
    if(not country_set.empty):
        if(country_set.shape[0]==1):
            return country_set.iloc[0,0]
        
        else: # trouble: we have more than one match : check if any is forced !
            sub_country_set = country_set[country_set.Forced ==1]
            if(not sub_country_set.empty):
                if(sub_country_set.shape[0]==1):
                    return sub_country_set.iloc[0,0]
            else: 
                return "Unspecified"

            
    #If we reach here, nothing strictly matched (1-1) (either more than one non-forced thing or more 
    #      than one forced thing did).           
    return "Unknown"

def country_name_filter(name, countries):
    res = []
    empty = True
    name_list = name.split(',')
    for name_part in name_list:
        name_found = country_name_filter_apply(name_part, countries)
        if ((name_found != "Unknown") & (name_found != "Unspecified")):
            res.append(name_found)
            empty = False
    if(empty):
        res = ["Unknown"]
    return res

def remove_language_indicators(df, column_name):
    """

    :param df:
    :param column_name:
    :return:
    """
    df[column_name] = df[column_name].map(lambda x: x.split(':', max_split=1))
        