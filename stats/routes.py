from stats import app
from flask import render_template
from stats.leagues import league_table
from stats.fixtures import get_fixt
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/fixtures')
def fixtures_page():

    return render_template('fixtures.html', games=get_fixt())

@app.route('/tables')
def tables_page():

    return render_template('tables.html', table=league_table("E", 1, 23))