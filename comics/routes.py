from flask import render_template, url_for, flash, redirect, request
from comics import app
from comics.forms import LoginForm,RegistrationForm
from comics import requests


@app.route('/')
@app.route('/home')
def home():
     heroes = requests.get_superhero()
     
     return render_template('home.html',heroes=heroes)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
      
            return redirect(url_for('home'))
    else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('register.html', title='Login', form=form)
   
