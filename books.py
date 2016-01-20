import json, urllib2, utils, re

#google books api key: AIzaSyC3JS6akFEzmQqhsa_ny3OoqEt3gDOAWow
#link: https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=AIzaSyC3JS6akFEzmQqhsa_ny3OoqEt3gDOAWow
#GOOD READS
#key: SBrrYwqTUdPBlX6AF0Zbg
#secret: eZqmFsmb5HLwymmgTnxMCumMdvxyRTQ2MlZeBbcXmHI

def searchBook(query):
    """
    Searches a book by a String query using google books API

    Params:
         query: a String of what you want to search

    Returns:
         A list of dictionaries, each dictionary containing a book's info, 
         including title, authors, description, ISBN
         and average rating of the book
         Keys:
              title (string)
              authors (list containing list)
              desc (string)
              ISBN (int)
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
        if 'title' and 'description' in book['volumeInfo'].keys():
            traits['title']=book['volumeInfo']['title']
            traits['authors']=book['volumeInfo']['authors']
            traits['desc']=book['volumeInfo']['description']
            traits["ISBN"]=int(book['volumeInfo']['industryIdentifiers'][0]['identifier'])
            bookList.append(traits)
            ctr+=1
    return bookList

def getWidgetHelper(text):
    """
    Pulls out the widget from text

    Params:
         text: a String that includes the iframe widget within it

    Returns:
         newlist[0]: first and only result, containing a string that is the widget
"""
    widget = ""
    exp = """(<style>[\S\s]*</div>[\S\s]*</div>)"""
    newlist = re.findall(exp, text)
    return newlist[0]

def getBookReview(isbn):
    """
    Returns iframe review widget of the reviews of the book from GoodReads

    Params:
         isbn: 13 digit integer

    Returns:
         Returns iframe review widget. Basically HTML code
    """
    url="""
https://www.goodreads.com/book/isbn?isbn=%s&key=SBrrYwqTUdPBlX6AF0Zbg
    """
    url=url%(str(isbn))
    request_url = urllib2.urlopen(url) #ERROR HERE
    result = request_url.read()
    widget = getWidgetHelper(result)
    return widget

#print searchBook("the hunger games")
print getBookReview(9780552564267)
