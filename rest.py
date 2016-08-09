import urllib
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2

# url = 'http://www.acme.com/products/3222'
# response = urllib2.urlopen(url).read()

url = 'http://ip.jsontest.com'
params = urllib.parse.urlencode({
  'firstName': 'John',
  'lastName': 'Doe'
})
binary_params = params.encode()

response = urllib2.urlopen(url, binary_params).read()
print(response)
