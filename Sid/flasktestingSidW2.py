from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for
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
emailarray = []



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


app = Flask(__name__)

@app.route('/metastasis')
def my_form2():
    print "hi"
    
    return render_template("metastasis.html")

@app.route('/results', methods=['GET', 'POST'])
def my_form2_post():
    # global emailarray
    # theemail = emailarray[int(request.form['submit'])]       
    # emailID = int(request.form['submit'])
    return str(request.path)
    return str(request.form)

@app.route('/')
def my_form():
    
    return render_template("bananaFinale.html")



@app.route('/', methods=['POST'])
def my_form_post():
    global firstname
    global lastname
    global middlei
    global location
    global emailarray
    global fromaddr
    global subject
    #return str(request.form)
    firstname = request.form['firstname']
    middlei = request.form['middleinitial']
    lastname = request.form['lastname']
    location = request.form['location']
        

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
            
        emailarray = emails
        t = '''
        msg = MIMEText("Dear Rutgers Student, \n Your Rutgers ID has been found in: " + location + "! \n Please come by to pick it up! \n \n Yours Truly, \n RuFound ")
        msg['From'] = fromaddr
        msg['To'] = emailarray[0]
        msg['Subject'] = subject

        
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, emailarray[0], msg.as_string())
        server.quit() '''

        #return render_template("bananaFinale.html")
        
    
        Omega = open('templates\\metachunk.txt','r') #Top half of HTML File
        tau1 = Omega.read() #grabbed the top chunk
        Omega.close()
                
        Omega = open('templates\\beta1.txt','r')
        tau2 = Omega.read()
        Omega.close()

        Omega = open('templates\\beta2.txt','r')
        tau3 = Omega.read()
        Omega.close()

        Omega = open('templates\\beta21.txt','r')
        tau31 = Omega.read()
        Omega.close()
        
        Omega = open('templates\\beta3.txt','r')
        tau4 = Omega.read()
        Omega.close()

        Omega = open('templates\\lochunk.txt','r')
        tau5 = Omega.read()
        Omega.close()

        open('templates\\metastasis.html','w').close() #emptied
    
        i = 0
        w = ""
        while(i < len(names)):
            w = w + tau2 +  str(i) + tau3 + pics[i] + tau31 + names[i] + tau4 + "\n"
            i += 1

        Beta = open('templates\\em.txt','r')
        tau7 = Beta.read()
        Beta.close()

        
        w = tau1 + w + tau5 #head and drop

        Omega = open('templates\\metastasis.html','w')
        Omega.write(w)
        Omega.close()
        return redirect(url_for('my_form2'))
        
        #return render_template("metastasis.html")	'''
        return render_template("bananaFinale.html")

    else: #if no matches found
        i = 0
        return render_template("bananaFinale.html")
    

if __name__ == '__main__':
	app.run(debug=True)
