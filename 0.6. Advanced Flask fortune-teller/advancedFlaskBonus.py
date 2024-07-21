from flask import Flask, render_template, request, redirect, url_for
import random
app=Flask(__name__ ,template_folder='templates')

@app.route("/", methods=['GET', 'POST'])
def home():
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
	
	if request.method=='GET':
		return render_template("home.html")
	else:
		birthMonth=request.form["birthMonth"]
		bmLength=len(birthMonth)
		if bmLength>len(fortunes):
			monthFortune=fortunes[9]
		else:
			monthFortune=fortunes[bmLength-1]	
		return render_template("fortune.html",yourFortune=monthFortune)



if __name__ == '__main__':
	app.run(debug=True)