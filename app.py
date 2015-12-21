from flask import Flask, render_template,request
import utils, urllib2, json, random

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
