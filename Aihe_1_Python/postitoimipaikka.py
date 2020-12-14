import json
import urllib.request

print('Kirjoita postinumero: ')
postNum = input()

with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
    data = response.read()
    postinumerot = json.loads(data)

    if postNum in postinumerot:
        print(postinumerot[postNum])
    elif postNum not in postinumerot:
        print('Syötit virheellisen numeron')
