from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/admin')
def admin():
    return render_template('admin.html', title='Admin')

@app.route('/login')
def admin():
    return render_template('login.html', title='Login')

@app.route('/user')
def admin():
    return render_template('userProfile.html', title='Profile')
