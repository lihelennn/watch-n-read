from pymongo import MongoClient
from bson.objectid import ObjectId

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

def newComment(username, comment, postID):
    connection = MongoClient()
    db = connection.wnr

    db.comments.insert_one({postID:{"username":username, "comment": comment}})

def getCommentsByPostID(postID):
    connection = MongoClient()
    db= connection.wnr
   # db.wnr.remove({})
    cursor=db.comments.find()
    comments=[]
    for doc in cursor:
        comments.append(doc[postID])
    return comments
            

#newPost("Tony","hai","post here")
#newPost("Tony","nothing","post here1")
#newPost("Tony","not","post here2")
#newPost("Mario","hai","post here")
#newPost("Bowser","hai","....5")
#newPost("Wario","wow","waaahhhh")
#newPost("Luigo","rio","riiiiiiiiiiiiiio")
newComment("tony","this sucks","569920747fc12f2059eea253")
getCommentsByPostID("569920747fc12f2059eea253")
