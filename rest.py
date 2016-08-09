import pycurl
from io import BytesIO
import sys
import json
import urllib.parse as urllib

params = {}
params['type'] = 123
params['limit'] = 123
params['start'] = 0
params['access_token'] = "5fad6ce4eeca28c7fbd41f16073dc2e4f67f823b925d40ea3fc6bd8eb313b5723fdc7a0af0d65a01c52fefeaa35beec951e3ff4fe905d0a12a1342f5b070a313"

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

