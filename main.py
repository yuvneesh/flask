from flask import Flask
import functions as fn

app = Flask(__name__)

@app.route('/')
def main_function():
    return 'This is a main function, but modified'

app.add_url_rule('/date',view_func=fn.printDate)

if __name__ == '__main__':
    app.run(debug=True)
