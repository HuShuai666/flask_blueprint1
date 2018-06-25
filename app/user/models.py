from app.ext import db


class User(db.Model):
    uid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),index=True,unique=True)
    # create_data=db.Column(db.DateTime,nullable=True)
    # status=db.Column(db.Boolean)
    # desc=db.Column(db.Text)