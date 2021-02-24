# Agenda-X is a ToDo App built with Python 3.8, Flask and SQLDB
# This app was programmed and designed by Robert Miller

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)