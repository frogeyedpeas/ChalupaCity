from flask import Flask
from flask import request
from flask import render_template
import pymongo
from pymongo import MongoClient
import smtplib
from email.mime.text import MIMEText

fromaddr = 'rutgerslostandfound@gmail.com'
toaddrs = '' 
subject = 'Your RUID has been found'
username = 'rutgerlostandfound'
password = 'chalupacity'

location = ''

URI = "mongodb://admin:chalupacity@ds041651.mongolab.com:41651/rufound"
client = MongoClient(URI)
db = client.rufound
collection = db.namelist
firstname = ""
middlei = ""
lastname = ""
name = ""

app = Flask(__name__)

@app.route('/')
def my_form():
    
    return render_template("bananaFinale.html")

def dbInsert(name, email, url):
    global collection
    collection.insert({"name" : name, "email" : email, "url": url})
def verify():
	global firstname
	global middlei
	global lastname
	global name

	name = firstname + " " + middlei + " " + lastname
	
	matches = db.namelist.find_one({"name" : name}) 
	if matches == None:
		return False 
	else:
		return True

def getMatches():
	matches = db.namelist.find({"name" : name})
	return matches



@app.route('/', methods=['POST'])
def my_form_post():
	global firstname
	global lastname
	global middlei
   
	firstname = request.form['firstname']
	middlei = request.form['middleinitial']
	lastname = request.form['lastname']
	
	isValidStudent = verify()

	if isValidStudent == True:
		matches = getMatches()
		names = []
		emails = []
		pics = []
		count = 0
		for nameL in matches: #populate the arrays
			names.append(nameL["name"])
			emails.append(nameL["email"])
			pics.append(nameL["url"])
		return emails[0]		

	else: #if no matches found
		return "you done fucked up pussy"



if __name__ == '__main__':
	app.run(debug=True)
