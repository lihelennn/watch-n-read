from flask import Flask, render_template,request,session,redirect,url_for
import utils, urllib2, json, random, re

app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    else: 
        #data = request.form["info"]
        return redirect(url_for("/results", data = data))
    return render_template("index.html")
        
@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)

#tmdb api key https://api.themoviedb.org/3/movie/550?api_key=###
#0adca0f6cd83c5390b72d746f4df63e7
#example:http://api.themoviedb.org/3/search/movie?query=batman&api_key=0adca0f6cd83c5390b72d746f4df63e7

#key: ab64222e93da26b4aba758d80daa792810d18ecd for idreambooks
#link: http://idreambooks.com/api/books/reviews.json?q={keywords}&key={yourAPIkey}
