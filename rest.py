import pycurl
from io import BytesIO
import sys
import json


params = json.dumps([
  'type : 123',
  'limit : 123',
    'start : 0',
    'access_token : 123'
])
http_header = [
    'Content-Type: application/json',
    'Content-Length: ' + str(sys.getsizeof(params))
]

url = 'https://api.copernica.com/emailings/'

b = BytesIO()
c = pycurl.Curl()

c.setopt(pycurl.URL, url)
c.setopt(pycurl.WRITEDATA, b)
c.setopt(pycurl.HEADER, 1)
c.setopt(pycurl.CUSTOMREQUEST, "POST")
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, params)
c.setopt(pycurl.HTTPHEADER, http_header)

c.perform()
print(b.getvalue())
