import json, urllib2, utils
#tmdb api key https://api.themoviedb.org/3/movie/550?api_key=###
#0adca0f6cd83c5390b72d746f4df63e7

#key: ab64222e93da26b4aba758d80daa792810d18ecd for idreambook
#link: http://idreambooks.com/api/books/reviews.json?q={keywords}&key={yourAPIkey}

#LibraryThing key: 4a17e93e48c8dee63d4b797ab52458bf
#link: http://www.librarything.com/services/rest/1.1/?[method_name]& [arguments as key=value separated by ampersands]&apikey=[your developer key]



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
    movieList=[]
  
    for movie in r['results']:
        traits={}
        traits['title']=movie['original_title'].encode('utf-8')
        traits['overview']=movie['overview'].encode('utf-8')
        traits['id']=movie['id']
        movieList.append(traits)


    return movieList
#def searchBook(name):
searchMovie('harry%20potter')

def getReview(id):
    url="""
    https://api.themoviedb.org/3/review/%s/?api_key=0adca0f6cd83c5390b72d746f4df63e7
    """
    url=url%(id)

    request_url = urllib2.urlopen(url)
    result = request_url.read()
    r = json.loads(result)
    for movie in r['results']:
        print movie['media_title']+'\n'
        print movie['content']+'\n'


#spaceConverter("Blade Runner")
#https://api.themoviedb.org/3/review/<MOVIE ID NUMBER GOES HERE>/?api_key=0adca0f6cd83c5390b72d746f4df63e7
searchMovie('harry potter')
