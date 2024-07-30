from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# VARIABLES
TITLE = 'Home'
TEMPLATE = 'index.html'
LOGIN = 'login.html'


@app.route('/')
@app.route('/index')
def hello_world():
    user = {'username': 'Kaleigh'}
    posts = [
        {'author': {'username': 'Kaleigh'}, 'body': 'Beautiful day in London!'},
        {'author': {'username': 'Kenny'}, 'body': 'The Avengers movie is awesome'}
    ]
    return render_template(TEMPLATE, title=TITLE, user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template(LOGIN, title='Sign In', form=form)
