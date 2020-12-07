from flask import Flask, render_template
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'qwerty'
app.config['MYSQL_DB'] = 'movie'
app.config['MYSQL_PORT'] = '3306'
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/homepage')
def homepage():
    return render_template('home.html')

@app.route('/addmovie')
def addmovie():
    return render_template('addmovie.html')

@app.route('/addtimings')
def addtimings():
    return render_template('addtimings.html')


app.run(debug=True)
