from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime, timedelta
from tzlocal import get_localzone
import parsedatetime

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
    # @staticmethod
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

    # @staticmethod
    def convert_to_date(self, dateString):
        pdt_cal = parsedatetime.Calendar()
        time_struct, parse_status = pdt_cal.parse(dateString)
        return datetime(*time_struct[:6])

    def convert_text_to_event(self, text):
        date = None

        if 'duration' in text.entities:
            date = self.convert_to_date(text.entities['duration'])
        elif 'day' in text.entities and 'time' in text.entities:
            date = self.convert_to_date(text.entities['day'] + ' at ' + text.entities['time'])
        elif 'day' in text.entities:
            date = self.convert_to_date(text.entities['day'])
        elif 'time' in text.entities:
            date = self.convert_to_date(text.entities['time'])
        else:
            return False

        task = text.entities['task']

        self.addEvent(task, date, date, str(get_localzone()))
        return True
