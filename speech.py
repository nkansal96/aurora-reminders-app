import parsedatetime
import auroraapi as aurora
from datetime import datetime, timedelta
from auroraapi.speech import listen_and_transcribe
from auroraKeys import APP_ID, APP_TOKEN
from eventManager import EventManager

def convert_to_date(dateString):
    pdt_cal = parsedatetime.Calendar()
    time_struct, parse_status = pdt_cal.parse(dateString)
    return datetime(*time_struct[:6])

if __name__ == '__main__':
    # Set your application settings
    aurora.config.app_id    = APP_ID     # put your app ID here
    aurora.config.app_token = APP_TOKEN  # put your app token here

    print('PortAudio starting up...')
    text = listen_and_transcribe(silence_len=0.5)
    print('You said: {}'.format(text.text))

    interpretedText = text.interpret()
    date = None
    if 'duration' in interpretedText.entities:
        date = convert_to_date(interpretedText.entities['duration'])
    elif 'day' in interpretedText.entities:
        date = convert_to_date(interpretedText.entities['day'])
    elif 'time' in interpretedText.entities:
        date = convert_to_date(interpretedText.entities['time'])
    task = interpretedText.entities['task']

    eventMgr = EventManager()
    eventMgr.addEvent(task, date, date, 'UTC-07:00')