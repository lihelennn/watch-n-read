from flask import Flask, render_template,request,session,redirect,url_for
import utils, urllib2, json, random, re, books, movies

app = Flask(__name__)

#testing html template starts
@app.route("/index1")
def index1():
    return render_template("index1.html")
#testing html template ends

@app.route("/board", methods = ['GET','POST'])
def board():
    
@app.route("/new", methods = ['GET','POST'])
def new():
    if request.method=="GET":
        return render_template("new.html")
    else:
        uname=session['uname']
        title=request.form['title']
        line=request.form['entry']
        module.makePost(uname, title, line)
        #for multiple buttons
        #button=request.form['button']
        #if button=="Submit":
        return redirect('/thread/%s' %title)

@app.route("/thread", methods = ['GET','POST'])
@app.route("/thread/<title>", methods = ['GET','POST'])
def thread(title=''):
    



@app.route("/login", methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        uname = request.form['uname']
        pword = request.form['pword']
        #authentication goes here
        if uname == 'test' and pword == 'test':
            session['uname'] = uname;
            return redirect(url_for("index"))
        error = "Invaild username password combination"
        return render_template("login.html", error = error)
        
@app.route("/", methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    else:
        query = request.form["search"].encode('utf-8')
        #session['query']=query
        return redirect(url_for("results",query=query))
       
    return render_template("index.html")
        
@app.route("/results", methods = ['GET','POST'])
@app.route("/results/<query>", methods = ['GET','POST'])
def results(query=""):
  if request.method == 'GET':
      #query=request.args['query']
      #query=session['query']
      bookData=books.searchBook(query)
      movieData=movies.searchMovie(query)

      #???
      """
      bookInfo=""
      for book in bookData:
            bookInfo+=book['title']+'<br><br>'
            for a in book['authors']:
                bookInfo+=a.encode('utf-8')+'<br>'
            bookInfo+=book['desc']+'<br><br>'

      movieInfo=""
      for movie in movieData:
            movieInfo+=movie['title']+'<br><br>'
            movieInfo+=movie['overview']+'<br><br>'
      """
      return render_template("results.html", bookData = bookData, movieData=movieData)
  else:
      query = request.form["search"].encode('utf-8') 
      print query
      return redirect(url_for("results",query=query))

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
