from pymongo import MongoClient
from bson.objectid import ObjectId

"""
DATABASE SCHEMA

Users: username and password

Posts: username(of the poster) ; title ; content

Comments: username(of the commenter) ; content ; postID(of the post in which the comment resides)

"""


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

def getPostByPostID(postID):
    connection = MongoClient()
    db=connection.wnr
    a=ObjectId(postID)
    
    cursor=db.posts.find({'_id':ObjectId(postID)})
    for doc in cursor:
        return doc
    
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
        postlist.append( { 'postID':str(post['_id']), 
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
        postlist.append( { 'postID':str(post['_id']), 
                           'username': str(post['username']), 
                           'title':str(post['title']), 
                           'content':str(post['content']) } )
    return postlist

def getPostIDByUsernameTitle(username, title):
    """
    returns a string that is a posts objectID

    Params:
         username: a string that is the username of the poster
         
         title: a string that is the title of the post

    Returns:
         postID: a string that is the objectID of the post
    """

    postID = ""

    connection = MongoClient()
    db = connection.wnr
    
    username = username.lower()
    cursor=db.posts.find({"username": username, "title": title})

    for post in cursor:
        postID = str(post['_id'])
    return postID

def newComment(username, comment, postID):
    """
    Creates a new comment

    Params:
         username: a String of the commenter's username

         comment: a String of the comment's contents

         postID: a String of the id of the post

    Returns:
         VOID
    """
    connection = MongoClient()
    db = connection.wnr

    db.comments.insert_one({"username": username, "comment": comment, "postID": postID})

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
    cursor=db.comments.find({"postID":postID})
    
    comments=[]
    for com in cursor:
        comments.append(com)
    return comments

#newPost("Tony","hai","post here")
#newPost("Tony","nothing","post here1")
#newPost("Tony","not","post here2")
#newPost("Mario","hai","post here")
#newPost("Bowser","hai","....5")
#newPost("Wario","wow","waaahhhh")
#newPost("Luigo","rio","riiiiiiiiiiiiiio")
#newComment("tony","this sucks","569920747fc12f2059eea253")
#print getPostIDByUsernameTitle("Tony", "hai")
#print getPostByPostID(getPostIDByUsernameTitle("Tony", "hai"))
#newComment("David", "my first comment", getPostIDByUsernameTitle("Tony", "hai"))
#print getAllPosts()
#newPost("David", "mytitle", "mycontent")
#newComment("David", "comment1", getPostIDByUsernameTitle("David", "mytitle"))
#print getPostByPostID(getPostIDByUsernameTitle("David", "mytitle"))
#print getCommentsByPostID(getPostIDByUsernameTitle("David", "mytitle"))
