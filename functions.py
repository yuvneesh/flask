import datetime

def printDate():
    x = datetime.datetime.now()
    x = x.strftime("%B %d, %Y")
    return x

#Alternate to app.route decorator is the app.add_url_rule function. Both of these were tested succesfully here.
#app.add_url_rule('/date', view_func=printDate)