from flask import Flask, render_template
app = Flask(__name__)

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
