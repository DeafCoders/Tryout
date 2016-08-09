import pycurl
from io import BytesIO
import sys
import json
import urllib.parse as urllib


#Copernica API Class
class Copernica:

    def __init__(self):
       params = {}
       params['limit'] = 1  # limiet standaard 9999, geen beperking
       params['start'] = 0  # start altijd vanuit 0
       self.params = params
       self.details_url = {
           'statistics': '/statistics/?',
           'deliveries': '/deliveries/?',
           'destinations': '/destinations/?',
           'snapshot': '/snapshot/?',
       }
       self.temp = 0

    def curl_options(self, url):
        b = BytesIO()
        c = pycurl.Curl()

        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.VERBOSE, 0) #1 = debug aan, 0 = debug uit
        c.setopt(pycurl.WRITEDATA, b)

        c.perform()
        output_values = json.loads(b.getvalue().decode())
        return output_values

    def get_mailings(self, token, limit):

        if limit:
            self.params['limit'] = limit
        self.params['access_token'] = token
        self.params['type'] = 'mass'  # Type te kiezen uit bulk of mass
        return self.curl_options("https://api.copernica.com/emailings/?" + urllib.urlencode(self.params))

    def get_mailing_details(self, token, emailing_id, details):
        self.params['access_token'] = token
        return self.curl_options("https://api.copernica.com/emailing/" + str(emailing_id) + self.details_url[details] + urllib.urlencode(self.params))

    def get_mailings_mass(self, token, limit):
        count_id = self.get_mailings(token, limit)['data']

        for item in count_id:
            for item_details in self.details_url:
                print(self.get_mailing_details(token, item['id'], item_details))





#Ophalen alle mailings ahv token van een klant
#print(Copernica().get_mailings("5fad6ce4eeca28c7fbd41f16073dc2e4f67f823b925d40ea3fc6bd8eb313b5723fdc7a0af0d65a01c52fefeaa35beec951e3ff4fe905d0a12a1342f5b070a313"))
#ophalen statistieken ahv token van een klant
#print(Copernica().get_mailing_details("5fad6ce4eeca28c7fbd41f16073dc2e4f67f823b925d40ea3fc6bd8eb313b5723fdc7a0af0d65a01c52fefeaa35beec951e3ff4fe905d0a12a1342f5b070a313", "19", "snapshot"))

print(Copernica().get_mailings_mass("5fad6ce4eeca28c7fbd41f16073dc2e4f67f823b925d40ea3fc6bd8eb313b5723fdc7a0af0d65a01c52fefeaa35beec951e3ff4fe905d0a12a1342f5b070a313", 10))
