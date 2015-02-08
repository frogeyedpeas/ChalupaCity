#get info using full name
from pymongo import MongoClient
import sys

connection = MongoClient()
db = connection.rufound
collection = db.users

input = raw_input("Enter Full Name: ")

send = db.users.find({"fullname": input})

for result_object in send:
		print result_object
