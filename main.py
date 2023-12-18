from flask import *
from connector import initialize
app = Flask(__name__)  

db = initialize()

@app.route('/comet')
def message1():
    return render_template("index.html")

@app.route('/<n>/<no>')
def ran(n,no):
    return render_template("index.html",comet=n,improve=no)

@app.route('/add/<a>/<b>')
def add(a,b):
    return a+b

@app.route('/naya/<a>/<b>')
def addar(a,b):
    return str(int(a) + int(b))

# @app.route('/login')
# def login():
#     return render_template("login2.html")

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



@app.route('/test')
def test():
    users = db.child('users').shallow().get().val()
    return render_template("testing.html",user_list = users)


    

@app.route('/newlogin',methods=["GET","POST"])
def handle_get():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(username, password)
        data = request.form
        db_pass = db.child('users').child(data['username']).get()
        if(db_pass.val() == data['password']):
            return redirect("/comet")
        else :
            return render_template("login2.html",Message = "Invalid Credentials")
    else:   
        return render_template('login2.html')

    

@app.route('/newsignup',methods = ["GET","POST"])
def newsignup():
    if (request.method == 'POST'):
        data = request.form
        username = data['username']
        password = data['password']
        if(username in db.child('users').shallow().get().val()):
            print(db.child('users').shallow().get().val())
            return render_template("signup.html",Message = "Username already taken")
        elif(len(password)<6):
            return render_template("signup.html",Message = "Password must contain atleast 6 charaters")
        else:
            db.child('users').child(username).set(password)
            return redirect('/newlogin')
    else:
        return render_template('signup.html')            



@app.route('/signupread',methods = ["GET","POST"])
def signuppost():
    lao = request.form
    db.child('users').child(lao['username']).set(lao['password'])
    return redirect("/login")
    
    

@app.route('/api', methods = ["GET","POST"])
def apii():
    lao = request.json
    return jsonify({"name" : lao["firstname"] , "message" : "good"})

# @app.route('/signup')
# def signup():
#     return render_template("signup.html")
    
# @app.route('/loginread', methods=["GET","POST"])
# def loginread():
#     data = request.form
#     db_pass = db.child('users').child(data['username']).get()
#     if(db_pass.val() == data['password']):
#         return redirect("/comet")
#     else :
#         return redirect('/login')




if __name__ == '__main__':  
   app.run(debug = True) 