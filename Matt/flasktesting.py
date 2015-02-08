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

app = Flask(__name__)

@app.route('/')
def my_form():
    
    return render_template("bananaFinale.html")

def dbInsert(name, email, url):
    global collection
    collection.insert({"name" : name, "email" : email, "url": url})

@app.route('/', methods=['POST'])

<<<<<<< HEAD


    
=======
def verify():
	global firstname
	global middlei
	global lastname

	name = firstname + " " + middlei + " " + lastname
	print name

	matches = db.namelist.findOne({"name" : name}) 

	if matches == None:
		return True

	else:
		return False



>>>>>>> ab1799f4f04236a3d21bc6259f102aeb5b1f639a
def my_form_post():
    global firstname
    global lastname
    global middlei
   
   
    firstname = request.form['firstname']
    middlei = request.form['middleinitial']
    lastname = request.form['lastname']
<<<<<<< HEAD

    
    return render_template("bananaFinale.html")
	
=======
		
    s = verify()
    print (s)



>>>>>>> ab1799f4f04236a3d21bc6259f102aeb5b1f639a


	

if __name__ == '__main__':
	app.run(debug=True)
