import parsedatetime
import auroraapi as aurora
from datetime import datetime, timedelta
from auroraapi.speech import listen_and_transcribe
from auroraKeys import APP_ID, APP_TOKEN

def convert_to_utctime(dateString):
    pdt_cal = parsedatetime.Calendar()
    time_struct, parse_status = pdt_cal.parse(dateString)
    utc_delta = datetime.utcnow()-datetime.now()
    utc_time = datetime(*time_struct[:6]) + utc_delta
    return utc_time

if __name__ == '__main__':
    # Set your application settings
    aurora.config.app_id    = APP_ID     # put your app ID here
    aurora.config.app_token = APP_TOKEN  # put your app token here

    print('PortAudio starting up...')
    text = listen_and_transcribe(silence_len=0.5)
    print('You said: {}'.format(text.text))

    interpretedText = text.interpret()
    date = convert_to_utctime(interpretedText.entities['duration'])
    task = interpretedText.entities['task']