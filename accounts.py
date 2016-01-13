from pymongo import MongoClient

def isValid(username, password):
    connection=MongoClient()
    db=connection.wnr
    
    username=username.lower()
    cursor=db.users.find({'username':username, 'password': password})
    userlist=[]
    for doc in cursor:
        print doc
        for i in doc:
            userlist+=[str(i)]

    if 'username' and 'password' in userlist:
        return True
    return False

def newUser(username,password):
    connection = MongoClient()
    db = connection.wnr
    
    username = username.lower()
    cursor = db.users.find({'username':username,'password':password})

    userlist = []
    for doc in cursor:
        for i in doc:
            userlist += [str(i)]
    if 'username' in userlist:
        return False
    db.users.insert_one({"username":username,"password":password})
    return True

def newPost(username, title, post):
    connection = MongoClient()
    db=connection.wnr

    username=username.lower()
    db.posts.insert_one({"username": username, "title":title, "content":post})
    
def getPostsFromUser(username):
    connection = MongoClient()
    db = connection.wnr
    
    username = username.lower()
    cursor=db.posts.find({"username": username})
    postlist = []
    for posts in cursor:
        postlist += [ [ str(post['username']), str(post['title']), str(post['content']) ] ]
    return postlist

def getAllPosts():
    connection = MongoClient()
    db = connection.wnr

    cursor=db.posts.find()
    postlist=[]
    for post in cursor:
        print post
        postlist+=[ [ str(post['username']), str(post['title']), str(post['content']) ] ]
    return postlist


newPost("Tony","God","Hi my name is tony li")
newPost("Tony","What","this is bs....")
newPost("Tony","I am god","whyyyyyyyyy")
newPost("Mario","Luigi sucks","it's a me, mario")
newPost("Luigi","Mario sucks","waaaaa luigi")
newPost("Wario","war","whaaaaaaam")
newPost("Wario","io","whaaam")

print getAllPosts()
