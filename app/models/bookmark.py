from app import db

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
