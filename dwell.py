from flask import Flask, jsonify, render_template, request

import requests

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method=="POST":
	#	url = # insert API url here 
	#		+ request.form["user_search1"]
		response_dict = requests.get(url).json
		return render_template("results.html", api_data=response_dict)
	else:
		return render_template("search.html")

@app.errorhandler(404)
def notfound(error):
	return "Sorry, that page does not exist.", 404

if __name__== '__main__':
	app.run(host = '0.0.0.0')
