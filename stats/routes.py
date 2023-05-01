from stats import app
from flask import render_template
from stats.leagues import league_table, btts_table
from stats.fixtures import get_fixt


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/fixtures')
def fixtures_page():
    return render_template('fixtures.html', games=get_fixt())


@app.route('/tables/<cntry>')
def tables_page(cntry='E023'):
    return render_template('tables.html', table=league_table(cntry[0], cntry[1], int(cntry[-2:])))

@app.route('/btts/<cntry>')
def btts_page(cntry='E023'):
    return render_template('btts.html', table=btts_table(cntry[0], cntry[1], int(cntry[-2:])))

