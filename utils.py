import re, regex

def spaceConverter(query):
    newstring = ""
    for letter in query:
        if letter == " ":
            newstring += "%20"
        else:
            newstring += letter
    print newstring
    return newstring

def reviewEvaluation(text):
    ratio = 0
    exp = "[a-zA-Z]+"
    results = re.finall(exp, text)
    numofwords = len(results)
    
    exp = "([Nn]ot)|([Tt]oo)|([Dd]idn't)|([Dd]oesn't)|([B]bad)|([Tt]errible)"
    results = re.findall(exp, text)
    ratio = 1 - len(results)/numofwords
    return ratio
