import datetime

def printDate():
    x = datetime.datetime.now()
    x = x.strftime("%B %d, %Y")
    return x

#Unable to import and run functions with arguments
def square(n):
    return n**2