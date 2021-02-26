# Agenda-X is a ToDo App built with Python 3.8, Flask and SQLAlchemy
# This app was programmed and designed by Robert Miller

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    # show all tasks
    task_list = Task.query.all()
    return render_template('base.html', task_list=task_list)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)