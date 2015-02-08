from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for
import pymongo
from pymongo import MongoClient
import smtplib
from email.mime.text import MIMEText



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('minifile.html')

@app.route('/', methods=['POST'])
def my_form_post():
    return redirect(url_for('my_form2'))

@app.route('/a/')
def my_form2():
    return render_template('minifile2.html')
@app.route('/a/', methods=['POST'])
def my_form2_post():
    return str(request.form)
    
if __name__ == '__main__':
	app.run(debug=True)
