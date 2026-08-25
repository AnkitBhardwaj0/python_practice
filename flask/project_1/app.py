from flask import Flask, redirect,render_template,request,redirect,session
from db import Database
from api import API
app = Flask (__name__)
app.secret_key = 'my_secret_key'
dbo=Database()
api=API()
@app.route('/')# url create

def index():
     
     return render_template('login.html')

@app.route('/register')

def register():
     return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
     name=request.form.get('user_name')
     email=request.form.get('user_email')
     password=request.form.get('user_password')

     response=dbo.insert(name,email,password)

     if response:
          return render_template('login.html',message='registration successful . kindly login to proceed')
     else:
          return render_template('register.html',message='email already exists')

@app.route('/perform_login',methods=['post'])
def perform_login():
     email=request.form.get('user_email')
     password=request.form.get('user_password')

     response=dbo.search(email,password)
     if response:
          session['logged_in']=1
          return redirect('/profile')
     else:
          return render_template('login.html',message="incorrect email/password")

@app.route('/profile')
def profile():
     if session['logged_in']==1:
         return render_template('/profile.html')
     else:
          return redirect('/')

@app.route('/NER')
def NER():
     if session['logged_in']==1:
         return render_template('ner.html')
     else:
          return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
     if session['logged_in']==1:
         text=request.form.get('ner_text')
         print("TEXT:", repr(text))
         response=api.ner(text)
         print(response)
         
         return render_template('ner.html',response=response)
     else:
          return redirect('/')
app.run(debug=True)