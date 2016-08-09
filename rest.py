import pycurl
from io import BytesIO
import sys
import json


params = {
  'type': '123',
  'limit': '123',
    'start': '0',
    'access_token': '123'
}

url = 'https://api.copernica.com/emailings/'

b = BytesIO()
c = pycurl.Curl()

c.setopt(pycurl.URL, url)
c.setopt(pycurl.WRITEDATA, b)
c.perform()je
print(b.getvalue())
