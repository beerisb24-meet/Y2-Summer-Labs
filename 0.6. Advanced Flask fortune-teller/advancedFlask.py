from flask import Flask, render_template
import random
app=Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

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

	return render_template("fortune.html", yourFortune=fortunes[random.randint(0,9)])

if __name__ == '__main__':
	app.run(debug=True)