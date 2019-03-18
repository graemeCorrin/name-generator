from namegen.app import db
from sqlalchemy import BOOLEAN, String


class GivenName(db.Model):
    __tablename__ = 'given_name'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String())
    male = db.Column(BOOLEAN)
    female = db.Column(BOOLEAN)

    def __init__(self, name, male, female):
        self.name = name
        self.male = male
        self.female = female

    def __repr__(self):
        return '<id {}>'.format(self.id)
