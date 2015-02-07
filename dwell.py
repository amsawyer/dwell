# testing
from flask import Flask, jsonify, render_template, request
import requests
from mongokit import Connection, Document
# Configuration

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017


app = Flask(__name__)
app.config.from_object(__name__)

# connect to the database
connection = Connection(app.config['MONGODB_HOST'],
			app.config['MONGODB_PORT'])

app.config['DEBUG'] = True

# Defining MongoDB document

class city(Document):
	structure = {
		'name':unicode,
		'spr_temp':unicode,
		'sum_temp':unicode,
		'aut_temp':unicode,
		'win_temp':unicode,
	}
	validators={
		'name':max_length(50),
		'spr_temp': max_length(4),
		'sum_temp': max_length(4),
		'aut_temp': max_length(4),
		'win_temp': max_length(4)

	}
	use_dot_notation = True
	def _repr_(self):
		return '<City %r>' % (self.name)
	connection.register([City])

# app routes

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method=="POST":
		url = # insert API url here 
			+ request.form["user_search1"]
		response_dict = requests.get(url).json
		return render_template("results.html", api_data=response_dict)
	else:
		return render_template("search.html")

@app.errorhandler(404)
def notfound(error):
	return "Sorry, that page does not exist.", 404

if __name__ = '__main__':
	app.run(host = '0.0.0.0')
