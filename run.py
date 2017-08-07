import os
from flask import Flask, render_template, request
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
    message = None
    message_level = ''
    if request.method == 'POST':
        email = request.form.get('email')
        fighter_id = request.form.get('fighter')
        if email and fighter_id:
            user = db.session.query(User).filter_by(email=email).first()
            if user:
                message_level = 'info'
                message = 'You have already voted!'
            else:
                user = User(email=email)
                db.session.add(user)
                fighter = db.session.query(Fighter).filter_by(id=fighter_id).first()
                vote = Vote(user=user, fighter=fighter)
                db.session.add(vote)
                db.session.commit()
                message_level = 'success'
                message = 'Your vote for {} has been submitted!'.format(fighter.name)
        else:
            message_level = 'danger'
            message = 'You must enter your email and select a fighter to cast a vote.'
    fighters = Fighter.query.all()
    return render_template('index.html', message=message, message_level=message_level, fighters=fighters)


if __name__ == '__main__':
    app.run(debug=True)
