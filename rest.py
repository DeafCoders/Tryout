import pycurl
from io import BytesIO
import sys
import json
import urllib.parse as urllib

params = {}
params['type'] = 123
params['limit'] = 123
params['start'] = 0
params['access_token'] = 123

params = json.dumps(urllib.urlencode(params))
print(params)
http_header = [
    'Content-Type: application/json'
]

url = 'https://api.copernica.com/emailings/?%s' % params

b = BytesIO()
c = pycurl.Curl()

c.setopt(pycurl.URL, url)
c.setopt(pycurl.VERBOSE, 1)
c.setopt(pycurl.WRITEDATA, b)

c.perform()
output_values = json.loads(b.getvalue().decode())
print(type(output_values))
print(output_values["error"])

