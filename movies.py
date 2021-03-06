import json, urllib2, utils
#tmdb api key https://api.themoviedb.org/3/movie/550?api_key=###
#0adca0f6cd83c5390b72d746f4df63e7

def searchMovie(query):
    """
    Searches a movie by a String query using TMDB API

    Params:
         query: a String of the name of the movie

    Returns:
         A list of dictionaries that have the title, overview and id of the movie
    """
    name = utils.spaceConverter(query)
    url="""
    https://api.themoviedb.org/3/search/movie/?api_key=0adca0f6cd83c5390b72d746f4df63e7&query=%s
    """
    url=url%(name)

    request_url = urllib2.urlopen(url)
    result = request_url.read()
    r = json.loads(result)

    if (r['total_results']==0):
        return -1
    
    movieList=[]
  
    for movie in r['results']:
        traits={}
        traits['title']=movie['original_title']
        traits['overview']=movie['overview']
        traits['id']=movie['id']
        movieList.append(traits)
    return movieList

def getMovieReview(id):
    """
    Returns reviews using TMDB movie ID

    Params:
         ID: an integer we get from searchMovie()

    Returns:
         A list of dictionary reviews, containing the keys 'name' and 'content'
    """
    url = """
    https://api.themoviedb.org/3/movie/%s/reviews?api_key=0adca0f6cd83c5390b72d746f4df63e7
    """
    url=url%(str(id))

    request_url = urllib2.urlopen(url) ##ERROR HERE
    result = request_url.read()
    r = json.loads(result)
    rlist = r['results']
    reviewlist = []
    for review in rlist:
        data = {}
        data['author'] = review['author']
        data['content'] = review['content']
        reviewlist.append(data)
    return reviewlist

#print getMovieReview(49026)

#movieData=searchMovie('harry potter')
#for movie in movieData:
#    print movie["id"]
#    print movie["title"]
#    print getMovieReview(movie["id"])
