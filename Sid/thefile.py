from bs4 import BeautifulSoup
import urllib2 as u
import requests as r


payload = {"inputs":"Matt Lee"}


f = r.post("http://search.rutgers.edu/index.html", params=payload)



soup = BeautifulSoup(f.text)

print soup


