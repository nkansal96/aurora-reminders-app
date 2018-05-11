"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

class Reminder:
    def __init__(self):
        # Setup the Calendar API
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('calendar', 'v3', http=creds.authorize(Http()))

    # eventStart and eventEnd are strings representing a date of the following format: YYYY-MM-DDTHH:MM:SS-HH:MM
    # For example, the following date '2018-05-28T09:00:00-07:00' interprets as
    # May 28, 2018 at 9:00 am UTC-7 hours
    def addEvent(self, eventName, eventStart, eventEnd):
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        event = {}
        event['summary'] = eventName
        event['start'] = {'dateTime': eventStart}
        event['end'] = {'dateTime': eventEnd}
        event = self.service.events().insert(calendarId='primary', sendNotifications=True, body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))

reminder = Reminder()
reminder.addEvent('Test event', '2018-05-28T09:00:00-07:00', '2018-05-28T17:00:00-07:00')