from flask import Flask, render_template,request,session,redirect,url_for
import utils, urllib2, json, random, re, books, movies

app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    else:
        query = request.form["search"]
        session['query']=query
        return redirect(url_for("/results",query=query))
       
    return render_template("index.html")
        
@app.route("/results")
def results():
      query=request.args['query']
      query=session['query']
      bookData=books.searchBook(query)
      movieData=movies.searchMovie(query)

      bookInfo=""
      for book in bookData:
            bookInfo+=book['title']+'\n\n'
            bookInfo+=book['authors']+'\n\n'
            bookInfo+=book['desc']+'\n\n'

      movieInfo=""
      for movie in movieData:
            movieInfo+=movie['title']+'\n\n'
            movieInfo+=movie['overview']+'\n\n'
      return render_template("results.html", bookInfo = bookInfo, movieInfo=movieInfo)

if __name__ == "__main__":
   app.debug = True
   app.secret_key="watch-n-read"
   app.run(host="0.0.0.0", port=8000)

#takes string, returns dictionary with keys: title, author, desc(description)
#books.searchBook(query)

#takes string, returns dictionary with keys: title, overview, id
#movies.searchMovie(query)

#uses id to get review, returns ???
#movies.getReview(id)



#tmdb api key https://api.themoviedb.org/3/movie/550?api_key=###
#0adca0f6cd83c5390b72d746f4df63e7
#example:http://api.themoviedb.org/3/search/movie?query=batman&api_key=0adca0f6cd83c5390b72d746f4df63e7

#key: ab64222e93da26b4aba758d80daa792810d18ecd for idreambooks
#link: http://idreambooks.com/api/books/reviews.json?q={keywords}&key={yourAPIkey}
