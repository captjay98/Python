
# xml

import xml.etree.ElementTree as ET

input = '''

<stuff>
  <users>
    <user x="5">
       <id>008</id>
       <name>Jay</name>
    </user>
    <user x="6">
       <id>009</id>
       <name>CAP</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User Count', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute:', item.get("X"))
