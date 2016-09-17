#import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

#app.config.from_object(__name__)



#define views
@app.route("/")
def receivePage():
	return render_template('receivePage.html', a="asdf")

@app.route("/input")
def inputPage():
	return render_template('inputPage.html')