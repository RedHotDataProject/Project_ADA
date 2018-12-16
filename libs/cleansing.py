from collections import Counter
#from translate import Translator

class SmartLookup(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return key.title()
        return key


def to_lookup(dictionary):
    """
    Generates dictionary with keys and values exchanged.
    :param dictionary:
    :return: dictionary
    """
    lookup  = SmartLookup()

    for key, values in dictionary.items():
        for value in values:
            lookup[value] = key

    return lookup


def filter_others(key, values_list):
    """
    Returns key if key is in values list, else returns 'Other'.
    :param key:
    :param values_list:
    :return: values_list
    """
    if key in values_list:
        return key
    else:
        return 'Other'


def apply_country_name_filter(name, countries):
    """
    Harmonise country names.
    :param name:
    :param countries:
    :return: harmonised name
    """

    # No country name specified
    if name.lower() == "unknown":
        return "Unknown"

    # Try match from country name
    country_set_name = countries[countries.name.apply(lambda x: x.lower()  == name.lower())]
    if not country_set_name.empty and country_set_name.shape[0]==1:
        return country_set_name.iloc[0,0]

    # Try match from country code
    country_set_cca2 = countries[countries.cca2.apply(lambda x: str(x).lower()== name.lower())]
    if not country_set_cca2.empty and country_set_cca2.shape[0]==1:
        return country_set_cca2.iloc[0,0]

    # Try match from country alias
    country_set = countries[countries['alias'].str.contains(name, case=False)]
    if not country_set.empty:
        if country_set.shape[0]==1:
            return country_set.iloc[0,0]
        
        else: # trouble: we have more than one match : check if any is forced !
            sub_country_set = country_set[country_set.Forced ==1]
            if not sub_country_set.empty:
                if sub_country_set.shape[0]==1:
                    return sub_country_set.iloc[0,0]
            else: 
                return "Unspecified"

    # No match could be found
    return "Unknown"


def tag_filter(name, countries):
    """
    Clean country name str from special characters.
    :param name:
    :param countries:
    :return: name cleaned
    """
    res = []
    empty = True
    name_list = name.split(',')
    for name_part in name_list:
        if(name_part != ''):
            if(name_part[0]== " "):
                name_part = name_part[1:]
            if(name_part[-1]== " "):
                name_part = name_part[:-1]
            name_part = name_part.replace("(", "")
            name_part = name_part.replace("[", "")
            name_part = name_part.replace("{", "")
            name_part = name_part.replace("]", "")
            name_part = name_part.replace("}", "")
            name_part = name_part.replace(")", "")
            name_part = name_part.replace("?", "")
            if(name_part != ''):
                name_found = apply_country_name_filter(name_part, countries)
                if ((name_found != "Unknown") & (name_found != "Unspecified")):
                    res.append(name_found)
    
    return ",".join(res)

def clean_tags_for_regex(string):
    
    string_clean = []
    
    for token in string.split(","):
        token = token.replace("(", "")
        token = token.replace("[", "")
        token = token.replace("{", "")
        token = token.replace("]", "")
        token = token.replace("}", "")
        token = token.replace(")", "")
        token = token.replace("?", "")
        string_clean.append(token)

    return ",".join(string_clean)

def read_list_from_str(string):
    """
    Read a comma separated list from string.
    :param string as list
    :return: string as comma-separated list
    """
    res = []
    name = str(string)
    name = name.replace("'", "")
    list_name = name.strip("[]").split(", ")
    for name_part in list_name:
        res.append(name_part)
    return ",".join(res)


def remove_language_indicator(row_str):
    """
    Remove 'en_', 'fr_', etc. tags from column entries
    :param comma separated list of tags
    :param column_name:
    :return: comma separated list of tags
    """    
    tags = [tag if len(tag.split(':'))==1 else tag.split(':')[1] for tag in row_str.split(',')]
    
    return ",".join(tags)
    

def group_categories(categories_str, categories_lookup):
    """
    Find most common category group.
    :param categories_str:
    :param categories_lookup:
    :return: most common category
    """
    # Assign categories to group
    categories_grouped = [categories_lookup[z] for z in categories_str.split(',')]
    
    # Return most common category group (or first in case of tie) as the representive category
    return Counter(categories_grouped).most_common(1)[0][0]


def translate_columns(column):
    """
    Translate a column from german to english.
    :param column german:
    :return: column english
    """
    translated_column = []
    translator = Translator(from_lang="german",to_lang="english")
    for i in range(len(column)):
        element = column.iloc[i]
        element_translated = translator.translate(element)
        translated_column.append(element_translated)
        
    return translated_column
