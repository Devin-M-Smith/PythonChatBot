import string

def fixIt(x):
    x = x.lower()
    punctuation= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for a in punctuation:
        x = x.replace(a, "")
    return x
