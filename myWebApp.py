from flask import Flask, render_template
import functions as fn


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

app.add_url_rule('/date',view_func=fn.printDate)

# The code below did not work
#app.add_url_rule('/square/<n>',view_func=fn.square(n))

@app.route('/square/<int:n>')
def square_func(n):
    return fn.square(n)

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

if __name__ == '__main__':
    app.run(debug=True)
