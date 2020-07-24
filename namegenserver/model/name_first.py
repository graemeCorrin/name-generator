from namegenserver.app import db
from sqlalchemy import BOOLEAN, String


class NameFirst(db.Model):
    __tablename__ = 'name_first'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(String())
    male = db.Column(BOOLEAN)
    female = db.Column(BOOLEAN)

    def __init__(self, value, male, female):
        self.value = value
        self.male = male
        self.female = female

    def __repr__(self):
        return '<id {}>'.format(self.id)
