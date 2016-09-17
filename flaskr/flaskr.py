import os

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

#from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('server.key')
#context.use_certificate_file('server.crt')

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#lul we lazy
messages = []

#define views
@app.route("/")
def receivePage():
    if 'logged_in_user' in session:
        return render_template('receivePage.html', name=session['logged_in_user'])
    else:
        return redirect(url_for('login'))

@app.route("/inputPage", methods=['GET', 'POST'])
def inputPage():
    global messages
    error = None
    if request.method == 'POST':
        if 'title' in request.form and 'desc' in request.form and 'rad' in request.form:
            if messages:
                messages.append(request.form['title'])
            else:
                messages = [request.form['title']]
        else:
            error = 'Form not filled completely'
    return render_template('inputPage.html', error=error)

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
            session['logged_in_user'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('receivePage'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in_user', None)
    flash('You were logged out')
    return redirect(url_for('receivePage'))

if __name__ == '__main__':
    context = ('server.crt', 'server.key')
    app.run(ssl_context=context, threaded=True, debug=True)