from homeapp import app, db
from homeapp.models import User, DB
from flask import render_template, url_for, flash, redirect
from homeapp.forms import RegistrationForm, LoginForm
import datetime


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About Us')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    db = DB()
    if form.validate_on_submit():
        if(db.userExist(form.email.data)):
            flash(f'{form.email.data} already exists!')
            return render_template('register.html', title='Register', form=form)
        else:
            user = User(form.username.data, form.email.data, form.password.data, datetime.date.today())
            if(db.addUser(user.buildJSON())):
                flash(f'Account created for {form.username.data}!', 'success')
            else:
                flash('Failed to create account!', 'danger')
            return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    db = DB()
    if form.validate_on_submit():
        if(db.userExist(form.email.data)):
            found_user = db.getUser(form.email.data)
            if form.password.data == found_user['password']:
                flash(f"You have been logged in!", 'success')
                return redirect(url_for('home'))
            else:
                flash(f'Login Unsuccessful. Password Incorrect.', 'danger')
        else:
                flash(f'{form.email.data} not found. Try a different email or register below.', 'danger')
    return render_template('login.html', title='Login', form=form)
