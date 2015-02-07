from bs4 import BeautifulSoup
import urllib2 as u
import requests as r


payload = {"inputs","Matt Lee"}

f = r.get("http://search.rutgers.edu/index.html")
f = r.post("http://search.rutgers.edu/index.html")


soup = BeautifulSoup(f.text)


exit
print soup


