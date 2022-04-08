import requests
from bs4 import BeautifulSoup
from urllib import parse

# page 1: load first page
URL = "https://rdv.rhone.gouv.fr/eAppointment_PREF69_NAT_DEMANDE/appointment.do?preselectservice=DEPOT"
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'})
r = session.get(URL)
print(r.url)

soup = BeautifulSoup(r.text, features="html.parser")
print(r.url)

# get jsessionid
jsess = (parse.urlparse(r.url).params).split("=")[1]
print(jsess)

# step2: go to appointment page
r = session.get("https://rdv.rhone.gouv.fr/eAppointment_PREF69_NAT_DEMANDE/element/jsp/appointment.jsp;jsessionid=" + jsess)
print(r.text)

# TODO step3: check if 1 available spot

# TODO step4: send email
