from flask import *  
app = Flask(__name__)  



@app.route('/comet')
def message1():
    return "Hello World!"

@app.route('/<n>/<no>')
def ran(n,no):
    return render_template("index.html",comet=n,improve=no)

@app.route('/add/<a>/<b>')
def add(a,b):
    return a+b

@app.route('/naya/<a>/<b>')
def addar(a,b):
    return str(int(a) + int(b))

@app.route('/login')
def login():
    return render_template("login2.html")

@app.route('/readpost',methods=["GET","POST"])
def readerpost():
    data = request.form
    print(data["username"])
    return "welcome" + data["username"]

@app.route('/readget',methods=["GET","POST"])
def readerget():
    data = request.args
    print(data["username"])
    return "welcome" + str(data["username"])








@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signupread',methods = ["GET","POST"])
def signuppost():
    lao = request.form
    return str(lao['firstname'])

@app.route('/api', methods = ["GET","POST"])
def apii():
    lao = request.json
    return jsonify({"name" : lao["firstname"] , "message" : "good"})
    
if __name__ == '__main__':  
   app.run(debug = True) 