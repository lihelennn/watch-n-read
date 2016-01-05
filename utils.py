

def spaceConverter(query):
    newstring = ""
    for letter in query:
        if letter == " ":
            newstring += "%20"
        else:
            newstring += letter
    print newstring
    return newstring
