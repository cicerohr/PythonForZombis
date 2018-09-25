#

from tkinter import *
from sound_panel import *
import pygame.mixer
import os


def shutdown():
    mixer.stop()
    app.destroy()


app = Tk()
app.title("Musiquinhas")
mixer = pygame.mixer
mixer.init()
dirList = os.listdir(".")
for fname in dirList:
    if fname.endswith('.wav'):
        SoundPanel(app, mixer, fname).pack()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
