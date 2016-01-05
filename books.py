import json, urllib2, utils

#google books api key: AIzaSyC3JS6akFEzmQqhsa_ny3OoqEt3gDOAWow
#link: https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=yourAPIKey

def searchBook(query):
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
