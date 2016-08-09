import pycurl
from io import BytesIO
import sys
import json
import urllib.parse as urllib

params = {}
params['type'] = 123
params['limit'] = 123
params['start'] = 0
params['access_token'] = "27009132287e614fa57f7b821c83ef27332c93ac2f5430c01b9b6471925458f8754b7a49f2c5f4fd5fc08cd5a74af155fdee4683977ad28c99668744c440e02a"

http_header = [
    'Content-Type: application/json'
]

url = "https://api.copernica.com/emailings/?" + urllib.urlencode(params)
print(url)
b = BytesIO()
c = pycurl.Curl()

c.setopt(pycurl.URL, url)
c.setopt(pycurl.VERBOSE, 1)
c.setopt(pycurl.WRITEDATA, b)

c.perform()
output_values = json.loads(b.getvalue().decode())
print(type(output_values))
print(output_values)

