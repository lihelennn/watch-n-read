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
##########################################################################

"""
"kind": "books#volumes",
 "totalItems": 27,
 "items": [
    {
   "kind": "books#volume",
    "id": "_oG_iTxP1pIC",
    "etag": "PaWqLaLOMjk",
    "selfLink": "https://www.googleapis.com/books/v1/volumes/_oG_iTxP1pIC",
    "volumeInfo": {
    "title": "Flowers for Algernon",
    "authors": [
     "Daniel Keyes"
    ],
    "publisher": "Houghton Mifflin Harcourt",
    "publishedDate": "2007-12-01",
    "description": "The beloved, classic story of a mentally disabled man whose experimental quest for intelligence mirrors that of Algernon, an extraordinary lab mouse.",
    "industryIdentifiers": [
     {
      "type": "ISBN_10",
      "identifier": "0547539630"
     },
     {
      "type": "ISBN_13",
      "identifier": "9780547539638"
     }
    ],
    "readingModes": {
     "text": true,
     "image": true
    },
    "pageCount": 304,
    "printType": "BOOK",
    "categories": [
     "Fiction"
    ],
    "averageRating": 4.0,
    "ratingsCount": 1456,
    "maturityRating": "NOT_MATURE",
    "allowAnonLogging": false,
    "contentVersion": "1.11.9.0.preview.3",
    "imageLinks": {
     "smallThumbnail": "http://books.google.com/books/content?id=_oG_iTxP1pIC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
     "thumbnail": "http://books.google.com/books/content?id=_oG_iTxP1pIC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    },
    "language": "en",
    "previewLink": "http://books.google.com/books?id=_oG_iTxP1pIC&printsec=frontcover&dq=flowers+for+algernon+inauthor:keyes&hl=&cd=1&source=gbs_api",
    "infoLink": "http://books.google.com/books?id=_oG_iTxP1pIC&dq=flowers+for+algernon+inauthor:keyes&hl=&source=gbs_api",
    "canonicalVolumeLink": "http://books.google.com/books/about/Flowers_for_Algernon.html?hl=&id=_oG_iTxP1pIC"
   },
   "saleInfo": {
    "country": "US",
    "saleability": "FOR_SALE",
    "isEbook": true,
    "listPrice": {
     "amount": 9.99,
     "currencyCode": "USD"
    },
    "retailPrice": {
     "amount": 9.99,
     "currencyCode": "USD"
    },
    "buyLink": "http://books.google.com/books?id=_oG_iTxP1pIC&dq=flowers+for+algernon+inauthor:keyes&hl=&buy=&source=gbs_api",
    "offers": [
     {
      "finskyOfferType": 1,
      "listPrice": {
       "amountInMicros": 9990000.0,
       "currencyCode": "USD"
      },
      "retailPrice": {
       "amountInMicros": 9990000.0,
       "currencyCode": "USD"
      }
     }
    ]
   },
   "accessInfo": {
    "country": "US",
    "viewability": "PARTIAL",
    "embeddable": true,
    "publicDomain": false,
    "textToSpeechPermission": "ALLOWED",
    "epub": {
     "isAvailable": true,
     "acsTokenLink": "http://books.google.com/books/download/Flowers_for_Algernon-sample-epub.acsm?id=_oG_iTxP1pIC&format=epub&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
    },
    "pdf": {
     "isAvailable": true,
     "acsTokenLink": "http://books.google.com/books/download/Flowers_for_Algernon-sample-pdf.acsm?id=_oG_iTxP1pIC&format=pdf&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
    },
    "webReaderLink": "http://books.google.com/books/reader?id=_oG_iTxP1pIC&hl=&printsec=frontcover&output=reader&source=gbs_api",
    "accessViewStatus": "SAMPLE",
    "quoteSharingAllowed": false
   },
   "searchInfo": {
    "textSnippet": "The beloved, classic story of a mentally disabled man whose experimental quest for intelligence mirrors that of Algernon, an extraordinary lab mouse."
   }
  },
"""
