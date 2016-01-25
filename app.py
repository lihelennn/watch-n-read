from flask import Flask, render_template,request,session,redirect,url_for
import utils, urllib2, json, random, re, books, movies, accounts

app = Flask(__name__)


@app.route("/board", methods = ['GET','POST'])
def board():
    if request.method=="GET":
        posts = accounts.getAllPosts()    
        return render_template("board.html",posts=posts)
    else:
        uname=session['uname']
        title=request.form['Title']
        line=request.form['text']
        accounts.newPost(uname, title, line)
        return redirect('/thread/%s' %title)


@app.route("/thread", methods = ['GET','POST'])
@app.route("/thread/<id>", methods = ['GET','POST'])
def thread(id=''):                    
    if request.method=="GET":
        post = accounts.getPostByPostID(id)
        comments = accounts.getCommentsByPostID(id)

        return render_template("thread.html", comments=comments, post=post)
    else:
        #needs a form
        content = request.form["text"]
        uname=session['uname']
        account.newComment(uname, content, id)
        return redirect(url_for("thread/%s" %(id)))
                        
@app.route("/create", methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        uname = request.form['uname']
        pword = request.form['pword']
        if accounts.newUser(uname,pword):
            msg="Success!"
            return render_template('create.html', msg=msg)
        else:
            msg="Failure!"
            return render_template('create.html', msg=msg)


@app.route("/login", methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        uname = request.form['uname']
        pword = request.form['pword']
        #authentication goes here
        if accounts.isValid(uname,pword):
            session['uname'] = uname;
            return redirect(url_for("index"))
        error = "Invaild username password combination"
        return render_template("login.html", error = error)
        
@app.route("/", methods = ['GET','POST'])
@app.route("/index1", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index1.html")

    else:
        query = request.form["search"].encode('utf-8')
        return redirect(url_for("results",query=query))
       
    return render_template("index1.html")
        
@app.route("/results", methods = ['GET','POST'])
@app.route("/results/<query>", methods = ['GET','POST'])
def results(query=""):
  if request.method == 'GET':

      bookData=books.searchBook(query)
      movieData=movies.searchMovie(query)
  
  for movie in movieData:
      reviews = movies.getMovieReview(movie["id"])
      if len(reviews) > 0:
          result=0
          for review in reviews:
              result+=utils.reviewEvaluation(review["content"])
              result/=len(reviews)
          if result < 0.5:
              movie["result"]="book"
          else:
              movie["result"]="movie"
     
          #movie["result"]=result


###regex stuff
#      utils.reviewEvaluation(text)

      return render_template("results.html", bookData = bookData, movieData=movieData)
  else:
      query = request.form["search"].encode('utf-8') 
      print query
      return redirect(url_for("results",query=query))

if __name__ == "__main__":
   app.debug = True
   app.secret_key="watch-n-read"
   app.run(host="0.0.0.0", port=8000)
