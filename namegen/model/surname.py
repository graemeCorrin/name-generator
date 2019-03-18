from namegen.app import db
from sqlalchemy import BOOLEAN, String


class SurName(db.Model):
    __tablename__ = 'surname'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String())
    lan = db.Column(String())

    def __init__(self, name, lan):
        self.name = name
        self.lan = lan

    def __repr__(self):
        return '<id {}>'.format(self.id)
