import json, urllib2
#tmdb api key https://api.themoviedb.org/3/movie/550?api_key=###
#0adca0f6cd83c5390b72d746f4df63e7

#key: ab64222e93da26b4aba758d80daa792810d18ecd for idreambook
#link: http://idreambooks.com/api/books/reviews.json?q={keywords}&key={yourAPIkey}

#LibraryThing key: 4a17e93e48c8dee63d4b797ab52458bf
#link: http://www.librarything.com/services/rest/1.1/?[method_name]& [arguments as key=value separated by ampersands]&apikey=[your developer key]
def searchMovie(name): 
    url="""
    https://api.themoviedb.org/3/search/movie/?api_key=0adca0f6cd83c5390b72d746f4df63e7&query=%s
    """
    url=url%(name)

    request_url = urllib2.urlopen(url)
    result = request_url.read()
    r = json.loads(result)
    for movie in r['results']:
        print movie['original_title']+'\n'
        print movie['overview']+'\n'
    
#def searchBook(name):
searchMovie('harry%20potter')


