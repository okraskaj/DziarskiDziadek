# -*- coding: utf-8 -*-
import json
from data import *
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
app.secret_key = "ADSOCXZ(@>?!)_2HA!xz.'[]"

def sort_events_by_date(events):
    sorted_events = sorted(events, key=lambda events: events['datetime'])
    return sorted_events

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/events/<category>', )
def return_events(category):
    events_in_category = []
    for event in events:
        if event['category'].__contains__(category):
            events_in_category.append(event)
    return json.dumps(events_in_category)

@app.route('/events/<event_id>')
def return_event(event_id):
    return 'event' + str(event_id)

@app.route('/categories/group')
def return_categories():
    return json.dumps(categories_group)

def add_events_to_categories():
    i = 0
    for event in events:
        for category in event['category']:
            events_lists[category].append(i)
        i = i + 1

events = sort_events_by_date(events)
# print events
add_events_to_categories()
# print events_lists

if __name__ == '__main__':
    app.run()



