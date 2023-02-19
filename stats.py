from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stats.db'
db = SQLAlchemy(app)



class Game(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    home = db.Column(db.String(), nullable=False)
    away = db.Column(db.String(), nullable=False)



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/fixtures')
def fixtures_page():
    games = [
        {'id': 1, 'home': "Nott'm Forest", 'away': 'Man City' },
        {'id': 2, 'home': "Man United", 'away': 'Leicester'},
        {'id': 3, 'home': "Chelsea", 'away': 'Southampton'},
    ]
    return render_template('fixtures.html', games=games)

@app.route('/tables')
def tables_page():
    table = [
        {'id': 1, 'team': 'Man City', 'played': 16, 'W': 10, 'D': 3, 'L': 3, 'GD': 24, 'PTS': 51},
        {'id': 2, 'team': "Man United", 'played': 16, 'W': 9, 'D': 5, 'L': 3, 'GD': 18, 'PTS': 48},
        {'id': 3, 'team': 'Leicester', 'played': 16, 'W': 8, 'D': 4, 'L': 3, 'GD': 4, 'PTS': 47},
        {'id': 4, 'team': 'Southampton', 'played': 16, 'W': 7, 'D': 3, 'L': 3, 'GD': -4,'PTS': 30},
        {'id': 5, 'team': 'Chelsea', 'played': 16, 'W': 8, 'D': 3, 'L': 2, 'GD': -24,'PTS': 25}
    ]
    return render_template('tables.html', table=table)
