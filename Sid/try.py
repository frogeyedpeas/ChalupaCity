from flask import Flask

x = open("phptestfile.html",'r')
w = x.read()
x.close()

app = Flask(__name__)

@app.route('/')
def hello():
    return w

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
