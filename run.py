import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

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

    fighters = Fighter.query.order_by('id').all()
    total_votes = db.session.query(Vote).count()
    vote_query = db.session.query(Vote.fighter_id, func.count(Vote.fighter_id))
    vote_counts = vote_query.group_by(Vote.fighter_id).order_by('fighter_id').all()

    return render_template('index.html', message=message, message_level=message_level,
                           fighters=fighters, total_votes=total_votes, vote_counts=vote_counts)


if __name__ == '__main__':
    app.run(debug=True)
