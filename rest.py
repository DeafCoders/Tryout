import pycurl
from io import BytesIO
import sys
import json
import urllib.parse as urllib


#Copernica API Class
class Copernica:

    def __init__(self):
       params = {}
       params['limit'] = -2  # limiet standaard 1
       params['start'] = 0  # start altijd vanuit 0
       self.params = params
       self.details_url = {
           'statistics': '/statistics/?',
           'deliveries': '/deliveries/?',
           'destinations': '/destinations/?',
           'snapshot': '/snapshot/?',
       }

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

    def get_mailings_mass(self, token, limit=1):
        count_id = self.get_mailings(token, limit)['data']
        for item in count_id:
            for item_details in self.details_url:
                print(self.get_mailing_details(token, item['id'], item_details))

    #todo: functie bouwen om alle waarden in database te invoeren aan hand van mailing ID (1: ID ontvangen en aanroepen met get_mailing_details , 2: waarden uit dict extraheren, 3: waarden in database invoeren

    #todo: functie bouwen voor periodieke checks of er nieuwe mailings zijn verstuurd (1: timestanpsent van laatste mailing opzoeken via SQL, vanaf dat datum tot nu toe opzoeken, en vervolgens functie van TODO 1 aanroepen met nieuwe mailingIDs



