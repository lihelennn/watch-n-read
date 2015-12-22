from flask import Flask, request
import json, urllib2
#tmdb api key https://api.themoviedb.org/3/movie/550?api_key=###
#0adca0f6cd83c5390b72d746f4df63e7

#key: ab64222e93da26b4aba758d80daa792810d18ecd for idreambook
#link: http://idreambooks.com/api/books/reviews.json?q={keywords}&key={yourAPIkey}
"""
from urllib2 import Request, urlopen

headers = {
  'Accept': 'application/json'
}
request = Request('http://api.themoviedb.org/3/configuration', headers=headers)

response_body = urlopen(request).read()
print response_body"""

def search(name): 
    print "hi"
