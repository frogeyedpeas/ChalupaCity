from flask import Flask
from flask import request
from flask import render_template
import pymongo
from pymongo import MongoClient

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
    return render_template("bananas.html")

@app.route('/', methods=['POST'])

def my_form_post():
	global firstname
	global lastname
	global middlei

	textarray = []
	firstname = request.form['firstname']
	middlei = request.form['middlei']
	lastname = request.form['lastname']
	
	everything = db.namelist.find()

	return everything
	

if __name__ == '__main__':
	app.run(debug=True)
