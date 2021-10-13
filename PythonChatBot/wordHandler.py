import string

def fixIt(x):
    x = x.lower()
    x = x.translate(None, string.punctuation)
    return x
