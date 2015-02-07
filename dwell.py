from flask import Flask, jsonify, render_template, request
import requests
import cities
# Configuration

app = Flask(__name__)
app.config.from_object(__name__)

app.config['DEBUG'] = True

# app routes

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results", methods=["GET", "POST"]) 
def get_results():
    if request.method == "POST":
        spr_temp = request.form["input_spr"]
        summ_temp = request.form["input_summ"]
        aut_temp = request.form["input_aut"]
        win_temp = request.form["input_win"]
        print spr_temp
        print summ_temp
        print aut_temp
        print win_temp
        sorted_tup = cities.average(spr_temp, summ_temp, aut_temp, win_temp)
        return render_template("results.html", data=sorted_tup)

@app.errorhandler(404)
def notfound(error):
    return "Sorry, that page does not exist.", 404

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
