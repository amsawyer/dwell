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
		return render_template("results.html", api_data=response_dict)
	else:
		return render_template("search.html")

@app.route("/results",methods=["GET","POST"]}
def get_results():
    if request.method == "POST":
        spr_temp = request.form["input_spr"]
        summ_temp = request.form["input_summ"]
        aut_temp = request.form["input_aut"]
        win_temp = request.form["input_win"]
        
        return render_template("results.html")

@app.errorhandler(404)
def notfound(error):
	return "Sorry, that page does not exist.", 404

if __name__ = '__main__':
	app.run(host = '0.0.0.0')
