from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_function():
    return 'This is a main function'

if __name__ == '__main__':
    app.run()
