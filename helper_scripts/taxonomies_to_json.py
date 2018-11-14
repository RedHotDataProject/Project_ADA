import json

synonym_lookup = {}

with open("taxonomies.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

synonyms = []
for line in content:

    if line == "":
        if synonyms:
            synonym_lookup[synonyms[0]] = synonyms
        synonyms = []
    else:
        words = line.split(",")
        try:
            synonyms.extend([word.split(":")[-1] for word in line.split(",")])
        except IndexError:
            print("Ooops")

with open('taxonomies.json', 'w') as fp:
    json.dump(synonym_lookup, fp,
              sort_keys=True,
              indent=4,
              separators=(',', ': '))