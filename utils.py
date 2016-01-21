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

    exp = "([Yy]es)|([Gg]ood)|([Aa]wesome)|([Gg]reat)|([Bb]est)|([Aa]mazing)|([Ff]avorite)|([^s][Ll]ike)|([Aa]stonish)|([Bb]reathtaking)|([Ll]ove)|([Ww]onderful)|([Ee]ngaging)|([Hh]ighly recommended)|([Ww]ould recommend)|([Ee]njoy)|([Cc]an't wait)|([Ee]xciting)|([Ff]un)|([Cc]ool)"
    goodresults = re.findall(exp, text)
    ratio = len(goodresults)/numofwords

    exp = "([Nn]o)|([Nn]ot)|([Tt]oo)|([Dd]idn't)|([Dd]oesn't)|([Cc]an't)|([Cc]annot)|([B]bad)|([Tt]errible)|([Bb]oring)|([Ff]fail)|([Hh]orrible)|([Hh]orrendous)|([Pp]oor)|([Ss]hoddy)|([Ss]tupid)|([Uu]gly)|([Uu]npleasant)|([Aa]nnoy)|([Ii]nconsist)|([Hh]ard)|([Hh]ate)"
    badresults = re.findall(exp, text)
    badratio = len(badresults)/numofwords
    
    return ratio

#JAVASCRIPT NEEDED TO GET TEXT FROM IFRAME
#var myIFrame = document.getElementById("myIframe");
#var content = myIFrame.contentWindow.document.body.innerHTML;
