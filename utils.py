import re

def spaceConverter(query):
    newstring = ""
    for letter in query:
        if letter == " ":
            newstring += "%20"
        else:
            newstring += letter
    return newstring

def reviewEvaluation(text):
    """
    Will analyze the number of good/bad words and return a ratio good:bad
    Params:
        text - (String) Text coming from the content of the review
    Returns:
        ratio - (Float) A ratio of good to bad words
    """

    ratio = 0
    exp = "[a-zA-Z]+"
    results = re.finall(exp, text)
    numofwords = len(results)

    exp = "([Yy]es)|([Gg]ood)|([Aa]wesome)|([Gg]reat)|([Bb]est)|([Aa]mazing)"
    goodresults = re.findall(exp, text)
    
    exp = "([Nn]o)|([Nn]ot)|([Tt]oo)|([Dd]idn't)|([Dd]oesn't)|([B]bad)|([Tt]errible)"
    badresults = re.findall(exp, text)
    ratio = len(goodresults)/len(badresults)
    return ratio

