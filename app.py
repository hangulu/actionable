from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
import sqlite3
from sqlite3 import Error
from get_events import *

# Configure application
app = Flask(__name__)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
	response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	response.headers["Expires"] = 0
	response.headers["Pragma"] = "no-cache"
	return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def create_connection(db_file):
	""" Create a database connection to the SQLite database specified by the db_file
	db_file: database file
	return: Connection cursor or None
	"""
	try:
		c = sqlite3.connect(db_file)
		conn = c.cursor()
		return conn
	except Error as e:
		print(e)

	return None


#Establish connection
conn = create_connection('actionable.db')


@app.route("/")
def main():
	"""Render the homepage."""
	return render_template('index.html')

@app.route("/resources")
def resources():
	"""Render webpage for protest resources."""
	return render_template('resources.html')

@app.route("/news")
def news():
	"""Render webpage for news."""
	return render_template("news.html")

@app.route("/protests", methods=["GET", "POST"])
def protests():
	"""Find protests that fit the user's preferences and render the list of protests."""

	if request.method == "POST":
		# Get the protest parameters from the form
		issue = request.form.get("issue")
		timeframe = request.form.get("timeframe")
		zipcode = request.form.get("zipcode")

		# Check to see if the inputted zip code is for a valid place and extract the city name. If not, redirect them to the homepage.
		conn.execute("SELECT postal_code, place_name FROM places WHERE postal_code=?", (zipcode, ))
		row = conn.fetchone()
		if row is None:
			return redirect(url_for("index"))

		place_name = row[1]

		# Look up the events
		protests = lookup_event(issue, zipcode, place_name, timeframe)

		# Disaggregate the dataframe
		event_ids = protests['id'].tolist()
		event_names = protests['name'].tolist()
		event_descriptions = protests['description'].tolist()
		event_cities = protests['city'].tolist()
		num_events = len(event_ids) - 1

		# Render the template with the list of protests
		return render_template('list.html', ids=event_ids, names=event_names, descriptions=event_descriptions, cities=event_cities, num=num_events)
	else:
		return render_template('protests.html')
