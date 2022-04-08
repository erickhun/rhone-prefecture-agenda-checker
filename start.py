import requests
from bs4 import BeautifulSoup

# step 1: 
URL = "https://rdv.rhone.gouv.fr/eAppointment_PREF69_NAT_DEMANDE/appointment.do?preselectservice=DEPOT"
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'})
r = session.get(URL)

print(r.text)
soup = BeautifulSoup(r.text)
