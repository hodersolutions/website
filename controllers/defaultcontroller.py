from flask import redirect, render_template
from root import application

@application.route("/")
def index(*args, **kwargs):
	return render_template('index.html')

@application.route("/about")
def about(*args, **kwargs):
	return render_template('about.html')

@application.route("/careers")
def careers(*args, **kwargs):
	return render_template('careers.html')

@application.route("/contact")
def contact(*args, **kwargs):
	return render_template('contact.html')