from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase
app=Flask(__name__)
app.config['SECRET_KEY']='verysecret'
firebaseConfig = {
  "apiKey": "AIzaSyAEiW6C3bzhwGQrMAVaPsAW-bJBBoJF2To",
  "authDomain": "recipesindividualproject.firebaseapp.com",
  "projectId": "recipesindividualproject",
  "storageBucket": "recipesindividualproject.appspot.com",
  "messagingSenderId": "978436464786",
  "appId": "1:978436464786:web:eb62a51f1ff5f08184864b",
  "measurementId": "G-28D9NXM9KQ",
 "databaseURL":"https://recipesindividualproject-default-rtdb.europe-west1.firebasedatabase.app/" 
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
		name=request.form['name']
		user={"email":email, "password":password, "name":name}
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
			return redirect(url_for('home'))
		except:
			error="Something went wrong. try again."
			return render_template('signin.html', error=error)

@app.route('/signout')
def signout():
	login_session['user']=None
	auth.current_user=None
	return redirect(url_for('signin'))

@app.route('/addRecipe', methods=['GET', 'POST'])
def addRecipe():
	if request.method=="GET":
		return render_template('addRecipe.html')
	else:
		uid=login_session['user']['localId']
		recipeName=request.form['recipeName']
		notes=request.form['notes']
		ingredients=request.form['ingredients']
		instructions=request.form['instructions']
		name=db.child('Users').child(uid).child('name').get().val()
		recipe={'author':name, 'name':recipeName, 'notes':notes, 'ingredients':ingredients, 'instructions':instructions}
		db.child('Users').child(uid).child('recipe').set(recipe)
		db.child('Users').child('recipes').push(recipe)

		return redirect(url_for('home'))

@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method=='GET':
		uid=login_session['user']['localId']
		recipes=db.child('Users').child('recipes').get().val()
		return render_template('home.html', recipes=recipes)
	else:
		recipes=db.child('Users').child('recipes').get().val()
		recipeName=request.form['chooseRecipe']
		author=request.form['chooseRecipe']
		notes=recipes[recipeName]['notes']

		return redirect(url_for('showRecipe', name=recipeName))

@app.route('/showRecipe/<name>')
def showRecipe(name):
	return render_template('showRecipe.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)