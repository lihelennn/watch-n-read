import json, urllib2, utils

#google books api key: AIzaSyC3JS6akFEzmQqhsa_ny3OoqEt3gDOAWow
#link: https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=yourAPIKey

def searchBook(query):
    """
    Searches a book by a String query using google books API

    Params:
         query: a String of what you want to search

    Returns:
         A list of dictionaries that have the title, authors, and description
         of the book
         Keys:
              {
 "kind": "books#volumes",
 "items": [
  {
   "kind": "books#volume",
   "id": "_ojXNuzgHRcC",
   "etag": "OTD2tB19qn4",
   "selfLink": "https://www.googleapis.com/books/v1/volumes/_ojXNuzgHRcC",
   "volumeInfo": {
    "title": "Flowers",
    "authors": [
     "Vijaya Khisty Bodach"
    ],
   ...
  },
  {
   "kind": "books#volume",
   "id": "RJxWIQOvoZUC",
   "etag": "NsxMT6kCCVs",
   "selfLink": "https://www.googleapis.com/books/v1/volumes/RJxWIQOvoZUC",
   "volumeInfo": {
    "title": "Flowers",
    "authors": [
     "Gail Saunders-Smith"
    ],
    ...
  },
  {
   "kind": "books#volume",
   "id": "zaRoX10_UsMC",
   "etag": "pm1sLMgKfMA",
   "selfLink": "https://www.googleapis.com/books/v1/volumes/zaRoX10_UsMC",
   "volumeInfo": {
    "title": "Flowers",
    "authors": [
     "Paul McEvoy"
    ],
    ...
  },
  "totalItems": 3
}
    """
    name=utils.spaceConverter(query)
    url="""
    https://www.googleapis.com/books/v1/volumes?q=%s&key=AIzaSyC3JS6akFEzmQqhsa_ny3OoqEt3gDOAWow
    """
    url=url%(name)
    
    request_url = urllib2.urlopen(url)
    result = request_url.read()
    r = json.loads(result)
    bookList=[]
    ctr=0
    for book in r['items']:
        if ctr==10:
            break
        traits={}
        if 'title' in book['volumeInfo'].keys():
            traits['title']=book['volumeInfo']['title']
            traits['authors']=book['volumeInfo']['authors']
            traits['desc']=book['volumeInfo']['description']
            bookList.append(traits)
            ctr+=1

    return bookList
        
print searchBook("harry potter")
