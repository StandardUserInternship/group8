import os
from app import app, db
from flask import render_template, flash, redirect, url_for, request, abort, session
from app.forms import LoginForm, RegistrationForm, FileUploadForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, DataSets
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
import datetime
import csv

#Homepage

@app.route('/')
@login_required
def index():
    return render_template('index.html', title='Homepage')

#Submitting the file to be analyzed on homepage
@app.route('/', methods=['GET', 'POST'])
@login_required
def upload_files():
    chartTypes = ['singleLineChart', 'multiLineChart', 'barChart']
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploads_dir = os.path.join(app.instance_path, 'uploads')
            file_path = os.path.join(uploads_dir, filename)
            uploaded_file.save(file_path)

            data_file = DataSets(user_id=current_user.get_id(), file_name=filename, file_path=file_path)
            db.session.add(data_file)
            db.session.commit()
            
            os.rename(file_path, file_path + str(data_file.get_file_id()))
            session['filepath'] = file_path

            return redirect(url_for('results'))
    else:
        return render_template('index.html', title='Upload', chartTypes=chartTypes)

#Potential page to be taken to after submitting file?
@app.route('/results')
@login_required
def results():

    labels = []
    data = []
    
    with open(filepath, 'r') as csvfile:
        reader = csv.reader(filepath, delimiter=' ', )
        header = 0
        for row in reader:
            if header == 0:
                labels = row
                header = 1
            else:
                data.append(row)
    
    if selected == singleLineChart or selected == barChart:
        x_data = data[::2]
        y1_data = data[1::2]
        y2_data = data
    elif selected == multiLineChart:
        x_data = data[::3]
        y1_data = data[1::3]
        y2_data = data[2::3]

    return render_template('results.html', title='Results', selectedType=selected, axisLabels=labels, xData=x_data,
    y1Data=y1_data, y2_data=y2_data)

#Admin page. Only vieweable by admins
@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html', title='Admin')

#Login Page. Required for accessing every other page.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')    
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form, )

#Logout page. Only shows if logged in.
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#Register option at the bottom of login page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, account_type=0, date_created=datetime.datetime)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    
#User homepage. Possibly show uploaded files?
@app.route('/user')
@login_required
def userProfile():
    return render_template('userProfile.html', title='Profile')
