from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import sys

# Initialize the app
app = Flask(__name__)

# Load the config file
app.config.from_object('config')
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'users'
	
	username = db.Column(db.String(64), primary_key=True)
	name = db.Column(db.String(120))
	password_hash = db.Column(db.String(128))
	organiser = db.Column(db.Boolean, default=False)

	def __repr__(self):
	    return '<User {}>'.format(self.username)

class Event(db.Model):
	__tablename__ = 'events'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(140))
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime)
	owner = db.Column(db.String(128), db.ForeignKey('users.username'))

	def __repr__(self):
	    return '<Event {}>'.format(self.name)

class Attendee(db.Model):
	_tablename__ = 'attendees'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(128), db.ForeignKey('users.username'))
	event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

	def __repr__(self):
	    return '<Attendee {}>'.format(self.id)

def auth(user, password):
	user = User.query.filter_by(username=user).first()
	if not user:
		return None
	if user.organiser:
		return "organiser"
	else:
		return "user"

@app.route('/api/events', methods=['POST'])
def add_event():
	data = request.json
	if auth(data['auth']['username'], None) != "organiser":
		return "Access denied!", 403
	event = Event(name=data['event']['name'], start_date=data['event']['start_date'], 
		end_date=data['event']['end_date'], owner=data['auth']['username'])
	db.session.add(event)
	db.session.commit()

	return "created", 201

@app.route('/api/events', methods=['GET'])
def get_events():
	events = Event.query.all()

	response = {}
	for event in events:
		response[event.id] = {}
		response[event.id]['name'] = event.name
		response[event.id]['start_date'] = event.start_date
		response[event.id]['end_date'] = event.end_date
		response[event.id]['owner'] = event.owner

	return jsonify(response), 200

def main():
	db.create_all()
	db.session.commit()
	app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()

