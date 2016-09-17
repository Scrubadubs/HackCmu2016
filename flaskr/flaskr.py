import os

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

#from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('server.key')
#context.use_certificate_file('server.crt')

app = Flask(__name__)

#app.config.from_object(__name__)



#define views
@app.route("/")
def receivePage():
	return render_template('receivePage.html', a="asdf")

@app.route("/input")
def inputPage():
	return render_template('inputPage.html')

if __name__ == '__main__':
    context = ('server.crt', 'server.key')
    app.run(ssl_context=context, threaded=True, debug=True)
