"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))


# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
event = {}
event['summary'] = 'Test event'
event['start'] = {'dateTime': '2018-05-28T09:00:00-07:00', 'timeZone': 'America/Los_Angeles'}
event['end'] = {'dateTime': '2018-05-28T17:00:00-07:00', 'timeZone': 'America/Los_Angeles'}
event = service.events().insert(calendarId='primary', sendNotifications=True, body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))
