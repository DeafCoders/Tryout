import urllib
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2

# url = 'http://www.acme.com/products/3222'
# response = urllib2.urlopen(url).read()

url = 'http://www.acme.com/users/details'
params = str(urllib.parse.urlencode({
  'firstName': 'John',
  'lastName': 'Doe'
}))
response = urllib2.urlopen(url, params).read()
