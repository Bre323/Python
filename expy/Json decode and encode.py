# Encoding to JSON

import json

person = {"name": "Carlo", "age": 34, "city": "San diego", "has children": True, "titles": ["engineer", "programer"]}

personjson = json.dumps(person, indent=4)
print(personjson)

with open('per.json', 'w')as file:
    json.dump(person, file, indent=4)



# Decoding JSON

with open('per.json', 'r') as file:
    per = json.load(file)
    print(per)
