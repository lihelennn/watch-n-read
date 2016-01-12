from pymongo import MongoClient

def isValid(username, password):
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

newUser("Tony","wasd")
print isValid("Tony","wasd")

