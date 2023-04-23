import os
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import util

# get current app directory
basedir = os.path.abspath(os.path.dirname(__file__))

# create a Flask instance
app = Flask(__name__)
# define SQLAlchemy URL, a configuration parameter
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# The db object instantiated from the class SQLAlchemy represents the database and
# provides access to all the functionality of Flask-SQLAlchemy.
db = SQLAlchemy(app)

class Event(db.Model):
	__tablename__ = 'events'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	contacts = db.relationship('Contact', backref='contacts')
	def __repr__(self):
		return '<Event %r>' % self.name

class Contact(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64), unique=True, index=True)
	last_name = db.Column(db.String(64))
	email = db.Column(db.String(64))
	phone = db.Column(db.String(64))
	prefers_email = db.Column(db.Boolean)


	event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
	def __repr__(self):
		return '<Contact %r>' % self.first_name

@app.route('/')
def index():
	# locates all the subclasses of db.Model and creates corresponding tables in the database for them
	# brute-force solution to avoid updating existing database tables to a different schema


	return render_template('index.html')


@app.route('/api/get_events', methods=['GET'])
def get_user():
	return util.parse_contact(Contact.query.all())


# default page for 404 error
# e.g. undefined service: http://127.0.0.1:5000/aa
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404_error.html'), 404

# default page for 500 error
@app.errorhandler(500)
def server_error(e):
	print(e)
	return render_template('500_error.html'), 500


if __name__ == '__main__':
	app.debug = True
	ip = '127.0.0.1'
	app.run(host=ip)
