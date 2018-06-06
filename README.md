# Aurora Reminders App
Aurora Reminders is a voice-enabled reminders application built using Python and the Aurora SDK. Users can interact with a virtual chat assistant and use natural language to easily add reminders to their Google Calendar.

![Screenshot](/screenshots/screenshot.png)

## Features
- Transcribes recorded user speech into text
- Interprets natural language to create reminders in Google Calendar
- Responds to the user with synthesized speech

## Getting Started
**The Recommended Python version is 3.0+**
1. Clone this repository.

2. Install dependencies with `pip install -r requirements.txt`.

3. [Enable the Google Calendar API](https://developers.google.com/calendar/quickstart/python) and copy your `client_secret.json` to the root directory of this project.

4. Create an account with [Aurora](http://dashboard.auroraapi.com/).

5. Create a file named `auroraKeys.py` in the root directory.
```
APP_ID = YOUR_APP_ID
APP_TOKEN = YOUR_APP_TOKEN
```
6. Run the app using `python3 speech.py`.

## Main Dependencies
Here are some of the core dependencies used in this project. The full list of requirements is available in `requirements.txt`
- [Kivy](https://github.com/kivy/kivy)
- [Aurora Python SDK](https://github.com/auroraapi/aurora-python)
- [Google Client Library](https://github.com/google/google-api-python-client)
