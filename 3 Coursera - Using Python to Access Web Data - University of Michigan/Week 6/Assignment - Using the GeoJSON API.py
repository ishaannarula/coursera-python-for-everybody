import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://py4e-data.dr-chuck.net/json?"

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'key':'42', 'address':address})
    print("Retrieving", url)
    data = urllib.request.urlopen(url).read().decode()
    print("Retrieved", len(data),"characters")

    try:
        js = json.loads(data)
    except:
        js = None
#    print(json.dumps(js, indent=4))

    if not js or 'status' not in js or js['status']!= 'OK':
        print('==========Failure to Retrieve==========')
        continue

    print("Place id", js['results'][0]['place_id'])
