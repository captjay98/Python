
# xml

import xml.etree.ElementTree as ET

input = '''

<stuff>
  <users>
    <user x="5">
       <name>Jay</name>
       <id>008</id>
    </user>
    <user x="6">
       <name>CAP</name>
       <id>009</id>
    </user>
 </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User Count', len(lst))

for item in lst:
    print('Name:', stuff.find('name').text)
    print('Attribute:', item.get("X"))
    print('Id', item.find('id').text)
