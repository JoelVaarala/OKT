import json
import urllib.request

print('Kirjoita postitoimipaikka: ')
postTmp = input().upper()

with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
    data = response.read()
    postidata = json.loads(data)

    # postidata.values())=kaupungit    .keys())=postinumerot    .items())=postinumero+kaupunki

nums = []
for num, city in postidata.items():
    if city == postTmp:
        nums.append(num)

if len(nums) > 0:
    NumStr = ', '.join(map(str, nums))
    print('postinumerot : ' + NumStr)
else:
    print('Ei postinumeroita')
