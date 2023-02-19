from stats import db


class Game(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    home = db.Column(db.String(), nullable=False)
    away = db.Column(db.String(), nullable=False)