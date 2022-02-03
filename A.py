# Json

import json

data = '''[
{"id" : "98",
  "x" :"5",
  "name" : "Jamal"},
{"id" : "67",
  "x" : "6",
  "name" : "Ibrahim"
  }]'''

info = json.loads(data)
print('User Count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('id:', item["id"])
    print('Attribute', item['x'])
