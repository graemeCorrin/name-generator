from namegenserver.app import db
from sqlalchemy import String


class Adverb(db.Model):
    __tablename__ = 'adverb'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(String())

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<id {}>'.format(self.id)
