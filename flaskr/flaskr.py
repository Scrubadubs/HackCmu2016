#import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from flask.ext.login import LoginManager, UserMixin, login_required

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#define views
@app.route("/")
def receivePage():
	if (session['logged_in']):
		return render_template('receivePage.html', a="asdf")
	else:
		return redirect(url_for('login'))

#check the login form username and password against the hardcoded stuff
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('receivePage'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('receivePage'))




















@app.route("/input")
def inputPage():
	return render_template('inputPage.html')