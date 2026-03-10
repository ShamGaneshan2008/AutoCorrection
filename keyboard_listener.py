# keyboard_listener.py

from pynput import keyboard
from ai_engine import correct_sentence
from dictionary import is_custom
from popup_ui import show_popup

# It stores the current word
buffer = ""

def on_press(key):

    # global variable which make the variable to use anywhere in the code
    global buffer

    try:
        if key.char:
            buffer += key.char

    except AttributeError:
        pass

    if key == keyboard.Key.space:

        words = buffer.split()

        if len(words) == 0:
            return

        last_word = words[-1]

        if is_custom(last_word):
            return

        corrected = correct_sentence(buffer)

        if corrected != buffer:

            print("Before:", buffer)
            print("After :", corrected)

            show_popup()

        buffer = ""


listener = keyboard.Listener(on_press=on_press)