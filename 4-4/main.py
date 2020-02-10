import tkinter as tk
import swapi

# Define constants

SHIPS = "ships"
PEOPLE = "people"
PLANETS = "planets"
QUERY_TYPES = [SHIPS, PEOPLE, PLANETS]

# Define App class
class App(tk.Frame):

    def __init__(self, master=None ):
        pass

    # Build out the UI
    def create_widgets(self):
        pass

    # Implement Search from swapi
    def search(self):
        pass

# Initialize the Window and start the app
root = tk.Tk()
root.title("SWAPI")
app = App(master=root)
app.mainloop()
