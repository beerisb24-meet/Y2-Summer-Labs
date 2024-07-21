from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

app=Flask(__name__)
app.config['SECRET_KEY']='verysecret'

firebaseConfig = {"apiKey": "AIzaSyAIVFwO8DAcNvTATZABAUGDPb1YWJgn3dU",
"authDomain": "authenticationlab-7257f.firebaseapp.com",
"projectId": "authenticationlab-7257f",
"storageBucket": "authenticationlab-7257f.appspot.com",
"messagingSenderId": "673402144009",
"appId": "1:673402144009:web:830fa7bc802308d4967fd8",
"measurementId": "G-GC79GPDNRS",
"databaseURL":""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signup():
	if request.method=='GET':
		return render_template('signup.html')
	else:
		email=request.form['email']
		password=request.form['password']
		#try:
		login_session['user'] = auth.create_user_with_email_and_password(email, password)
		return redirect(url_for('/home'))
		#except:
		#	error = "Something went wrong. Try again"
		#	return render_template("signup.html",error=error)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method=='GET':
		return render_template('signin.html')
	else:
		return render_template('signin.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method=='GET':
		return render_template('home.html')
	else:
		login_session['quotes']=[]

@app.route('/thanks')
def thanks():
	return render_template('thanks.html')

@app.route('/display')
def display():
	return render_template('display.html')


if __name__ == '__main__':
    app.run(debug=True)