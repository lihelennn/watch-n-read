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
    Will analyze the number of good/bad words and return a ratio good:total
    Params:
        text - (String) Text coming from the content of the review
    Returns:
        ratio - (Float) A ratio of good to total words
    """

    ratio = 0
    exp = "[a-zA-Z]+"
    results = re.finall(exp, text)
    numofwords = len(results)

    exp = "([Yy]es)|([Gg]ood)|([Aa]wesome)|([Gg]reat)|([Bb]est)|([Aa]mazing)|([Ff]avorite)"
    goodresults = re.findall(exp, text)
    
    ratio = len(goodresults)/numofwords
    return ratio

#JAVASCRIPT NEEDED TO GET TEXT FROM IFRAME
#var myIFrame = document.getElementById("myIframe");
#var content = myIFrame.contentWindow.document.body.innerHTML;
