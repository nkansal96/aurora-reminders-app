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
Here are some of the core Python dependencies used in this project. The full list of requirements is available in `requirements.txt`
- [Kivy](https://github.com/kivy/kivy)
- [Aurora Python SDK](https://github.com/auroraapi/aurora-python)
- [Google Client Library](https://github.com/google/google-api-python-client)

Another requirement to get the audio working is ffmpeg. This can be downloaded [here](https://www.ffmpeg.org/download.html).  

## FAQ
**1. I'm having trouble installing Kivy**  
Depending on what version of Kivy you are trying to install, it requires a different version of the dependency Cython. In our app, we used Kivy==1.10.0 and Cython==0.26.1. Furthermore, SDL2 should be installed as certain functions in the Kivy library require it. For further issues, reference the Kivy installation guide [here](https://kivy.org/docs/installation/installation.html). 

**2. I have Kivy installed properly, but I'm still getting an error as follows:**  
```
X Error of failed request:  BadWindow (invalid Window parameter)
  Major opcode of failed request:  4 (X_DestroyWindow)
  Resource id in failed request:  0x0
  Serial number of failed request:  160
  Current serial number in output stream:  162
```
What worked for us is to disable multisampling. This can be done by editing the file ~/.kivy/config.ini and setting multisamples to 0. 

**3. I got the following warning: `UserWarning: Cannot access credentials.json: No such file or directory`. How can I get rid of it?**  
No need to worry about this. The credentials.json is created when you first log in and caches your information into the directory. This speeds up future log ins. Just make sure `client_secret.json` is in your current directory as the credentials will eventually expire. 
