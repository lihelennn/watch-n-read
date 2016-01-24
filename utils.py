import re, math

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
    results = re.findall(exp, text)
    numofwords = len(results)

    exp = "([Yy]es)|([Gg]ood)|([Aa]wesome)|([Gg]reat)|([Bb]est)|([Aa]mazing)|([Ff]avorite)|([^s][Ll]ike)|([Aa]stonish)|([Bb]reathtaking)|([Ll]ove)|([Ww]onder)|([Ee]ngaging)|([Hh]ighly recommended)|([Ww]ould recommend)|([Ee]njoy)|([Cc]an't wait)|([Ee]xciting)|([Ff]un)|([Cc]ool)|([Hh]ilarious)|([Pp]rofound)|([Ee]ntertaining)|([Bb]rillian)|([Aa]ppreciat)|([Ee]xhilarat)|([Mm]aster)|([Gg]rand)|([Ww]in[\s\.])|([Ww]elcome)|([Aa]uthentic)|([Ss]tunning)|([Ii]nnovat)|([Ii]mmense)|([Cc]harm)|([Ss]timulat)|([Aa]bsolute)|([Aa]dorable)|([Aa]dventure)|([Bb]eautiful)|([Bb]rav)|([Cc]lassic)|([Cc]reative)|([Dd]azzl)|([Dd]elight)|([Ee]legant)|([Ee]chanting)|([Ee]nergy|([Ee]xellent)|([Ee]xquisite)|([Ff]abulous))|([Ff]antastic)|([Gg]enius)|([Ii]mpress)|([Ii]nvent)|([Ii]ntell)|([Mm]arvel)|([Mm]oving)|([Ee]mot)|([Nn]ice)|([Nn]ovel)|([Pp]erfect)|([Pp]henom)|([Pp]leas)"
    goodresults = re.findall(exp, text)
    goodratio = 1.0 * len(goodresults)/numofwords

    exp = "([Nn]o[\s\.])|([Nn]ot)|([Tt]oo)|([Dd]idn't)|([Dd]oesn't)|([Cc]an't)|([Cc]annot)|([B]bad)|([Tt]errible)|([Bb]oring)|([Ff]fail)|([Hh]orrible)|([Hh]orrendous)|([Pp]oor)|([Ss]hoddy)|([Ss]tupid)|([Uu]gly)|([Uu]npleasant)|([Aa]nnoy)|([Ii]nconsist)|([Hh]ard)|([Hh]ate)|([Bb]other)"
    badresults = re.findall(exp, text)
    badratio = 1.0 - (1.0 * len(badresults)/numofwords)

    goodratio = math.sqrt(math.sqrt(goodratio))
    badratio = math.sqrt(math.sqrt(badratio))
    finalratio = (badratio + goodratio) / 2
    return finalratio

#JAVASCRIPT NEEDED TO GET TEXT FROM IFRAME
#var myIFrame = document.getElementById("myIframe");
#var content = myIFrame.contentWindow.document.body.innerHTML;
