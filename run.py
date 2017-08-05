import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE_URL is by default
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////tmp/test.db')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.email


class Fighter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('votes', lazy='dynamic'))
    fighter_id = db.Column(db.Integer, db.ForeignKey('fighter.id'))
    fighter = db.relationship('Fighter', backref=db.backref('votes', lazy='dynamic'))


@app.route('/', methods=['GET', 'POST'])
def homepage():
    fighters = Fighter.query.all()
    return render_template('index.html', fighters=fighters)


if __name__ == '__main__':
    app.run(debug=True)
