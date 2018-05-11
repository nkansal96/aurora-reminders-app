from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

class EventManager:
    def __init__(self):
        # Setup the Calendar API
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('calendar', 'v3', http=creds.authorize(Http()))

    # eventStart and eventEnd are datetime objects to be converted into the following format: YYYY-MM-DDTHH:mm:SS
    def addEvent(self, eventName, eventStart, eventEnd, timeZone):
        eventStart = eventStart.strftime('%Y-%m-%dT%H:%M:%S')
        eventEnd = eventEnd.strftime('%Y-%m-%dT%H:%M:%S')

        # Call the Calendar API
        event = {}
        event['summary'] = eventName
        event['start'] = {'dateTime': eventStart, 'timeZone': timeZone}
        event['end'] = {'dateTime': eventEnd, 'timeZone': timeZone}
        event = self.service.events().insert(calendarId='primary', sendNotifications=True, body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        