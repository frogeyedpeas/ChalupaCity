import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.nameDB
collection = db.nameList

def dbInsert(name, email, url):
	person = {name: [email, url]}
	collection.insert(person)

while(True):
	x = raw_input("Type in Name: ")
	name = x
	x = raw_input("Type in Email: ")
	email = x
	x = raw_input("Type in photo URL: ")
	url = x
	if name == "e" or email == "e" or url =="e":
		print "input not inserted"
		break
	dbInsert(name, email, )
	print "Entry inserted\n"
