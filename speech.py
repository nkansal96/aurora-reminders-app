from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

import auroraapi as aurora
from auroraapi.speech import listen_and_transcribe
from auroraapi.text import Text

import sys
import threading
from random import randint
from functools import partial
from eventManager import EventManager
from auroraKeys import APP_ID, APP_TOKEN

theme_color = [0.31, 0.89, 0.76, 1]
white_color = [1, 1, 1, 1]
black_color = [0, 0, 0, 1]
listen_msg = "Listening..."
confirmations = ['OK. ', 'Got it. ', 'Sure. ', 'Alright. ', '']
apologies = ["I'm sorry, I don't understand.", "I didn't understand that."]
cancel_intents = ['cancel', 'never mind', 'forget it', 'quit', 'restart', 'start over']

def get_random_confirmation():
    return confirmations[randint(0, len(confirmations) - 1)]

def get_random_apology():
    return apologies[randint(0, len(apologies) - 1)]

event_mgr = EventManager()

Builder.load_string('''
<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
''')


class ScrollableLabel(ScrollView):
    text = StringProperty("Hello. Ask me to set a reminder.\n")


class ChatApp(App):

    def build(self):

        main_box_layout = BoxLayout(orientation='vertical',
                                    padding=20,
                                    spacing=10)

        in_box_layout = BoxLayout(orientation='horizontal',
                                  spacing=10,
                                  size_hint_y=0.08)

        chat_view = ScrollableLabel()

        button = Button(text='Record',
                        size_hint_x=0.2,
                        background_color=theme_color,
                        color=white_color)

        # Interpret user input to retrieve entities for reminder creation
        def interpret_user_response(text):
            interpret = text.interpret()

            if interpret.intent != 'set_reminder':
                update_chat(get_random_apology())
                return False
            else:
                create_event(interpret)
                return True

        def create_event(interpret):
            update_chat("Creating your reminder: \"{}\".".format(interpret.entities['task'].capitalize()), confirm=True)
            event_mgr.convert_text_to_event(interpret)

        def play_text_callback(text, *largs):
            Text(text).speech().audio.play()

        def listen_callback(*largs):
            msg = listen_and_transcribe(silence_len=0.5)
            hide_listen_animation()

            if msg.text != '':
                update_chat(msg.text, is_user=True)
                interpret_user_response(msg)
            else:
                update_chat(get_random_apology())

        def record_user_response():
            show_listen_animation()
            Clock.schedule_once(listen_callback, 0)

        def show_listen_animation():
            button.text = listen_msg

        def hide_listen_animation():
            button.text = "Record"

        def update_chat(text, is_user=False, confirm=False):
            if is_user:
                chat_view.text += '> ' + text + '\n'
            else:
                response = ""
                if confirm:
                    response += get_random_confirmation()
                response += text

                Clock.schedule_once(partial(play_text_callback, response), 0)

                chat_view.text += response + '\n'

        button.bind(on_press=lambda x: record_user_response())

        main_box_layout.add_widget(chat_view)
        main_box_layout.add_widget(in_box_layout)

        in_box_layout.add_widget(button)

        return main_box_layout


if __name__ == "__main__":
    # Set your application settings
    aurora.config.app_id    = APP_ID     # put your app ID here
    aurora.config.app_token = APP_TOKEN  # put your app token here

    Config.set('graphics', 'width', '500')
    Config.set('graphics', 'height', '600')
    Config.write()

    ChatApp().run()
