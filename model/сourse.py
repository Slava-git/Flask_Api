from datetime import datetime as dt
from core import db
from model.base import Model
class Course(Model ,db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    quantity_of_lectures = db.Column(db.Integer)

    def __repr__(self):
        return '<Course names as {}>'\
            .format(self.name)