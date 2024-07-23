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
"databaseURL":"https://authenticationlab-7257f-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()

@app.route('/', methods=['GET', 'POST'])
def signup():
	if request.method=='GET':
		return render_template('signup.html')
	else:
		userId=login_session['user']['localId']
		email=request.form['email']
		password=request.form['password']
		full_name=request.form['full_name']
		username=request.form['username']
		user={"email":email, "password":password, "full_name":full_name, "username":username}
		db.child("Users").child(userId).set(user)
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)

			return redirect(url_for('home'))
		except:
			error = "Something went wrong. Try again"
			return render_template("signup.html",error=error)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method=='GET':
		return render_template('signin.html')
	else:
		email=request.form['email']
		password=request.form['password']
		try:
			login_session['user']=auth.sign_in_with_email_and_password(email, password)
			return render_template('home.html')
		except:
			error="Something went wrong. try again."
			return render_template('signin.html', error=error)

@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method=='GET':
		return render_template('home.html')
	else:
		uid=login_session['user']['localId']
		said_by=request.form['said_by']
		text=request.form['quote']
		quote={'said_by':said_by, 'text':text, 'uid':uid}
		db.child("Users").child("quotes").push(quote)
		return redirect(url_for('thanks'))

@app.route('/signout')
def signout():
	login_session['user']=None
	auth.current_user=None
	return redirect(url_for('signin'))

@app.route('/thanks')
def thanks():
	return render_template('thanks.html')

@app.route('/display')
def display():
	uid=login_session['user']['localId']
	quotes=db.child('Users').child('quotes').get().val()
	return render_template('display.html',quotes=quotes)


if __name__ == '__main__':
    app.run(debug=True)