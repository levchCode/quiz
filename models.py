from app import db


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

    options = db.relationship('Option', backref='question')

    def __init__(self, text):
        self.text = text

        
class Option(db.Model):
    __tablename__ = 'option'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    answers = db.relationship('Answer', backref='option')

    def __init__(self, text):
        self.text = text

class Answer(db.Model):
    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(255), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'))

    def __init__(self, user, option):
        self.user = user
        self.option_id = option