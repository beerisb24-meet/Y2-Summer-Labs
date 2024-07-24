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
		login_session['user']=None
		auth.current_user=None
		return render_template('signup.html')
	else:
		login_session['user']=None
		auth.current_user=None
		email=request.form['email']
		password=request.form['password']
		name=request.form['name']
		user={"email":email, "password":password, "name":name}
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			userId=login_session['user']['localId']
			db.child("Users").child(userId).set(user)

			return redirect(url_for('home'))
		except:
			error = "Something went wrong. Try again"
			return render_template("signup.html",error=error)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method=='GET':
		login_session['user']=None
		auth.current_user=None
		return render_template('signin.html')
	else:
		login_session['user']=None
		auth.current_user=None
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
		recipes=db.child('recipes').get().val()
		if recipes!=None:
			for i in recipes:
				if recipeName == recipes[i]['name']:
					return render_template('addRecipe.html', error="This recipe name already exists. Please choose a different name.", notes=notes, ingredients=ingredients, instructions=instructions)
				else:
					name=db.child('Users').child(uid).child('name').get().val()
					recipe={'author':name, 'name':recipeName, 'notes':notes, 'ingredients':ingredients, 'instructions':instructions}
					db.child('Users').child(uid).child('recipes').push(recipe)
					db.child('recipes').push(recipe)
					return redirect(url_for('home'))
		else:
			name=db.child('Users').child(uid).child('name').get().val()
			recipe={'author':name, 'name':recipeName, 'notes':notes, 'ingredients':ingredients, 'instructions':instructions}
			db.child('Users').child(uid).child('recipes').push(recipe)
			db.child('recipes').push(recipe)
			return redirect(url_for('home'))

@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method=='GET':
		uid=login_session['user']['localId']
		recipes=db.child('recipes').get().val()
		return render_template('home.html', recipes=recipes)
	else:
		recipes=db.child('recipes').get().val()
		recipeName=request.form['chooseRecipe']
		print(recipeName)
		print(recipes)
		if recipes!=None:
			print("recipes is not none")
			for i in recipes:
				print(recipes[i])
				if recipeName == recipes[i]['name']:
					print(f"recipeName: {recipeName}, id: {i}")
					recipeId=i
					return redirect(url_for('showRecipe', recipeId=recipeId))
					
		return render_template('home.html', error="There are no existing recipes.")

@app.route('/showRecipe/<recipeId>')
def showRecipe(recipeId):
	recipe= db.child('recipes').child(recipeId).get().val()
	return render_template('showRecipe.html', name=recipe['name'], author=recipe['author'], notes=recipe['notes'], ingredients=recipe['ingredients'], instructions=recipe['instructions'])

@app.route('/myRecipes', methods=['GET', 'POST'])
def myRecipes():
	if request.method=='GET':
		uid=login_session['user']['localId']
		user=db.child('Users').child(uid).child('name').get().val()
		recipes=db.child('Users').child(uid).child('recipes').get().val()
		print(uid)
		print(recipes)
		return render_template('myRecipes.html', user=user, recipes=recipes)
	else:
		recipes=db.child('Users').child(uid).child('recipes').get().val()
		recipeName=request.form['chooseRecipe']
		print(recipeName)
		print(recipes)
		if recipes!=None:
			print("recipes is not none")
			for i in recipes:
				print(recipes[i])
				if recipeName == recipes[i]['name']:
					print(f"recipeName: {recipeName}, id: {i}")
					recipeId=i
					return redirect(url_for('showRecipe', recipeId=recipeId))
					
		return render_template('home.html', error="There are no existing recipes.")

if __name__ == '__main__':
    app.run(debug=True)