from flask import Flask, render_template, request, redirect, url_for
import random
from flask import session as login_session
app=Flask(__name__ ,template_folder='templates')
app.config['SECRET_KEY']="SOMETHINGUNIQUEANDSECRET"


@app.route('/', methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		username=request.form['username']
		birthMonth=request.form["birthMonth"]
		login_session['username']=username
		login_session['birthMonth']=birthMonth
		return redirect(url_for('home', bm=birthMonth, un=username))

@app.route('/home/<bm>/<un>')
def home(bm,un):

	return render_template('home.html', bm=bm, un=un)


@app.route("/fortune")
def fortune():
	fortunes=["Something good will happen to you exactly at 3:17 pm tomorrow", 
	"You will discover something lifechanging in the next week",
	"Remember to try again if you fail", 
	"Be careful on Wednesday",
	"You will be extra lucky on Thursday",
	"You should spend more time with your family",
	"Don't board a rocket ship in the next week",
	"Don't get mad on Monday",
	"Try to finish all your work as soon as possible",
	"You will go through something difficult on Sunday"]
	bmLength=len(login_session['birthMonth'])
	if bmLength>len(fortunes):
		monthFortune=fortunes[9]
		login_session['fortune']=monthFortune
	else:
		monthFortune=fortunes[bmLength-1]	
		login_session['fortune']=monthFortune


	return render_template("fortune.html", yourFortune=monthFortune)

if __name__ == '__main__':
	app.run(debug=True)