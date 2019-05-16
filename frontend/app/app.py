from flask import *
import requests
import sys

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Pici Events')

@app.route('/events.html')
def events():
	r = requests.get('http://server:5000/api/events')
	all_events = []
	for id, event in r.json().items():
		all_events.append(event)

	print(all_events, file=sys.stderr)
	return render_template('events.html', the_title='Events', all_events=all_events)

@app.route('/new_event.html')
def new_event():
	return render_template('new_event.html', the_title='New Event')

@app.route('/handle_data', methods=['POST'])
def handle_data():
	content  = {"auth": {"username" : "admin"}}
	content['event'] = {}
	content['event']['name'] = request.form['name']
	content['event']['start_date'] = request.form['start_date']
	content['event']['end_date'] = request.form['end_date']

	requests.post("http://server:5000/api/events", json=content)
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)
