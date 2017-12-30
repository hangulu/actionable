"""
Module to extract relevant Facebook events.
Help from: https://towardsdatascience.com/how-to-use-facebook-graph-api-and-extract-data-using-python-1839e19d6999
"""
import urllib3
import facebook
import requests
import pandas as pd
import datetime

def lookup_event(issue, zipcode, place_name, timeframe):
	"""
	Function to find the relevant event.
	issue (string): The political issue being searched for.
	zipcode (string): The zipcode of the user.
	place_name (string): The name of the city.
	timeframe (string): The timeframe of the user's desired events.

	return: pandas dataframe of events
	"""

	# Facebook token
	token = 'EAACHs6TsNpYBAN7lLZAif448IFR3YP7HC6XSXOk2FzAkjmYdXrKJvUZBvvk212imfeZAQcufUqi7Scl039ZAhUAVrOfh9HcwSmJpIlebg8SvVfmtEgbmHSEULgVVGQ7eMqEvhrQ9LGpZBV55pP73MZBDxur8HyNayb2e9arK6nIQZDZD'

	# Access the Facebook events using the API
	graph = facebook.GraphAPI(access_token=token, version=2.7)

	# Limit the number of events to 10000.
	events = graph.request('/search?q={}&type=event&limit=10000'.format(issue))

	# Dictionary with all the data
	event_list = events['data']

	# Convert the data into a pandas dataframe
	events_df = pd.DataFrame.from_dict(event_list, orient='columns')
	events_df = events_df[['id', 'name', 'start_time', 'description', 'place']]

	# Disaggregate the places dictionary
	places = events_df['place'].apply(pd.Series)
	places2 = places['location'].apply(pd.Series)[['city', 'zip']]
	events3 = pd.concat([events_df, places2], axis=1)

	# Retain the city and the zip
	before_time = events3.drop(['place'], axis=1)

	# Replace the Nan's with 0's for simplicity
	before_time.fillna(0, inplace=True)

	# Calculate the desired timeframe
	now = datetime.datetime.now()
	current_date = now.isoformat()
	weeks = int(timeframe)
	future_limit = (now + datetime.timedelta(days=(7 * weeks))).isoformat()

	# Filter out events outside of the specified timeframe
	timed_events = before_time.loc[before_time['start_time'] < future_limit]

	# Filter out the events that don't have the keyword in their description or aren't in the place
	specific_events = timed_events.loc[(timed_events['description'].str.lower().str.contains(issue)) | (timed_events['name'].str.lower().str.contains('protest')) | (timed_events['description'].str.lower().str.contains('protest')) | (timed_events['city'].str.lower().str.contains(place_name)) | (timed_events['zip'] == zipcode)]

	# Present the first 5 results as the final results of the search
	final_events = specific_events.head()

	return final_events
