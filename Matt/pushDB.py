import pymongo
from pymongo import MongoClient

URI = "mongodb://admin:chalupacity@ds041651.mongolab.com:41651/rufound"

client = MongoClient(URI)

db = client.rufound
collection = db.namelist

def dbInsert(name, email, url):

	collection.insert({"name" : name, "email" : email, "url": url})

while True:
	x = raw_input("Type in Name: ")
	name = x
	x = raw_input("Type in Email: ")
	email = x
	x = raw_input("Type in photo URL: ")
	url = x
	if name == "e" or email == "e" or url =="e":
		print "input not inserted"
		
	dbInsert(name, email, url)

	send = db.namelist.find({"name": name})
	

	for result_object in send:
		print result_object["email"]
	
