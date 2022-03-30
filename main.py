from flask import Flask
import functions as fn


app = Flask(__name__)

@app.route('/')
def main_function():
    return 'This is a main function, but modified'

app.add_url_rule('/date',view_func=fn.printDate)

# The code below did not work
#app.add_url_rule('/square/<n>',view_func=fn.square(n))

@app.route('/square/<int:n>')
def square_func(n):
    return fn.square(n)

@app.route('/render-html')
def render_html():
    html = """
    <html>
    <body>
    <h1> This is a rendered page </h1>
    </body>
    </head>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True)
