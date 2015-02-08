from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("bananas.html")

@app.route('/', methods=['POST'])
def my_form_post():
	textarray = []
	string1 = request.form['firstname']
	#string2 = request.form['lastname']
   
	print string1
	return string1
	

if __name__ == '__main__':
    app.run()
