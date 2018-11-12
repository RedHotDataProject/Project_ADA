import json


def correct_countries_tags(df):

    countries_column = df['countries_en']

    # Load dictionary that maps to correct countries tags
    with open('country_replacement.json', 'r') as json_data:
        country_replacement = json.load(json_data)

    # Replace country tags for actual country name
    for index, countries in df['countries_en'].str.split(',').items():
        if isinstance(countries, float): continue
        country_name = []
        found = False
        for s in countries:
            if s in country_replacement.keys():
                found = True
                country_name.append(country_replacement[s])
            else:
                country_name.append(s)
        if found:
            df.loc[index, 'countries_en'] = ','.join(country_name)

    return df
