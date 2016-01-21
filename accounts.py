from pymongo import MongoClient
from bson.objectid import ObjectId

def isValid(username, password):
    """
    Validates username and password combo

    Params:
         username: a String of the user's username

         password: a String of the user's password

    Returns:
         True
              if valid combo
         False
              otherwise
    """
    connection=MongoClient()
    db=connection.wnr
    
    username=username.lower()
    cursor=db.users.find({'username':username, 'password': password})
    userlist=[]
    for doc in cursor:
        for i in doc:
            userlist+=[str(i)]

    if 'username' and 'password' in userlist:
        return True
    return False

def newUser(username,password):
    """
    Creates a new user

    Params:
         username: a String of the user's desired username

         password: a String of the user's desired password

    Returns:
         True
              if the username doesn't already exist
         False
              otherwise
    """
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
    """
    Creates a new post

    Params:
         username: a String of the poster's username

         title: a String of the post's title

         post: a String of the contents of the post

    Returns:
         VOID
    """
    connection = MongoClient()
    db=connection.wnr
    username=username.lower()
    db.posts.insert_one({"username": username, "title":title, "content":post})
    
def getPostsFromUser(username):
    """
    Gets a list of all posts and their information from a user

    Params:
         username: a String of the user's username

    Returns:
         A list of dictionaries.
         [ { 
              <String> id: 
              <String> title: 
              <String> content 
           },
           ... 
         ]
    """
    connection = MongoClient()
    db = connection.wnr
    
    username = username.lower()
    cursor=db.posts.find({"username": username})
    postlist = []
    for posts in cursor:
        postlist.append( { 'id':str(post['_id']), 
                           'title':str(post['title']), 
                           'content':str(post['content'])})
    return postlist

def getAllPosts():
    """
    Gets a list of all posts in the database

    Params:
         NONE

    Returns:
         A list of dictionaries.
         [ { 
              <String> id: 
              <String> username:
              <String> title: 
              <String> content 
           },
           ... 
         ]
    """
    connection = MongoClient()
    db = connection.wnr

    cursor=db.posts.find()
    postlist=[]
    for post in cursor:
        postlist.append( { 'id':str(post['_id']), 
                           'username': str(post['username']), 
                           'title':str(post['title']), 
                           'content':str(post['content']) } )
    return postlist

def newComment(username, comment, postID):
    """
    Creates a new comment

    Params:
         username: a String of the poster's username

         comment: a String of the comment's contents

         postID: a String of the id of the post

    Returns:
         VOID
    """
    connection = MongoClient()
    db = connection.wnr

    db.comments.insert_one({postID:{"username":username, "comment": comment}})

def getCommentsByPostID(postID):
    """
    Gets all the comments of a post based on postID.

    Params:

         postID: a String of the id of the post

    Returns:
         A list of dictionaries.

         [
          {
               'username':
               'comment':
          },
          ...
         ]
    """
    connection = MongoClient()
    db= connection.wnr
   # db.wnr.remove({})
    cursor=db.comments.find()
    comments=[]
    for doc in cursor:
        comments.append({'username':str(doc[postID]['username']),
                         'comment':str(doc[postID]['comment'])})
    return comments
            

newPost("Tony","hai","post here")
newPost("Tony","nothing","post here1")
newPost("Tony","not","post here2")
newPost("Mario","hai","post here")
#newPost("Bowser","hai","....5")
#newPost("Wario","wow","waaahhhh")
#newPost("Luigo","rio","riiiiiiiiiiiiiio")
#newComment("tony","this sucks","569920747fc12f2059eea253")
#print getCommentsByPostID("569920747fc12f2059eea253")
print getAllPosts()
