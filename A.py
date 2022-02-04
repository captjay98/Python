#

import urllib.request
import urllib.parse
import urllib.error
import json

serviceurl = 'http://maps.googleapis.com/api/geocode/json?'

while True:
    address = input('Enter location:')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    ur = urllib.request.urlopen(url)
    data = ur.read().decode()
    print('Retrived', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== fAILURE TO RETIVE ===')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, "lng", lng)
    location = js['results'][0]['formatted_address']
    print(location)
