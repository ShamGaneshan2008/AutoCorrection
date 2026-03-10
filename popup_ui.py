import webbrowser
import os


def show_popup():

    file_path = os.path.abspath("templates/popup.html")

    webbrowser.open(f"file://{file_path}")