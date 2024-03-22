from flask import Flask,render_template,redirect,request,url_for
import mysql.connector

app=Flask(__name__)

conn=mysql.connector.connect(host="localhost",username='root',password='',database='payment')
cursor=conn.cursor()
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/register",methods=['POST','GET'])
def register():
    try:
        msg=''
        if request.method=="POST":
            name=request.form['name']
            email=request.form['email']
            pwd=request.form['pwd']
            phn=request.form['phn']
            sql="insert into register(username,email,password,phonenumber)value('%s','%s','%s','%s')"%(name,email,pwd,phn)
            print(sql)
            cursor.execute(sql)
            conn.commit()
            msg="Thank you for your register"
            return render_template("register.html",msg=msg)
        else:
            msg="you have not register"
            return render_template("register.html",msg=msg)
    except Exception as e:
        return render_template("register.html",msg=e)





@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/home1")
def home1():
    return render_template("home1.html")

if __name__=="__main__":
    app.run(debug=True)

