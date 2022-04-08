import requests
import time
from bs4 import BeautifulSoup
from urllib import parse


session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'})


# page 1: load first page
r = session.get("https://rdv.rhone.gouv.fr/eAppointment_PREF69_NAT_DEMANDE/appointment.do?preselectservice=DEPOT")
print(r.url)

print("Page1 - " + r.url)
print(r.headers)
print(r.status_code)
print("\n")

# get jsessionid
jsess = (parse.urlparse(r.url).params).split("=")[1]

# TODO step2: go to select type of appointment page
# This step doesn't work yet. 
#  In the chrome network tabs, there are multiple calls. 
# Not sure which one is needed to get to the next page

data= {"previousValueId": False}
r = session.post("https://rdv.rhone.gouv.fr/eAppointment_PREF69_NAT_DEMANDE/step1ScenarioTwo.do;jsessionid=" + jsess, data=data, allow_redirects=True)
print("Page2 - " + r.url)
print(r.headers)
print(r.status_code)

# TODO step3: select wanted option

# TODO step4: go to appointment page

# TODO step5 check if 1 available spot

# TODO step6: send email


# soup = BeautifulSoup(r.text, features="html.parser")
