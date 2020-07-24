from namegenserver.app import db
from sqlalchemy import String


class Adjective(db.Model):
    __tablename__ = 'adjective'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(String())

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<id {}>'.format(self.id)
