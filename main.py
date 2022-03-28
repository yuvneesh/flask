from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def main_function():
    return 'This is a main function, but modified'

@app.route('/date')
def printDate():
    x = datetime.datetime.now()
    x = x.strftime("%B %d, %Y")
    return x

#Alternate to app.route decorator is the app.add_url_rule function. Both of these were tested succesfully here.
#app.add_url_rule('/date', view_func=printDate)

if __name__ == '__main__':
    app.run(debug=True)
