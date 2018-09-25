# 1.1 - TWP452 Interface GUI Show Calouros 02
# Vamos aprender conceitos como GUI (interfaces gráficas) com Python
import pygame.mixer
from tkinter import *


def espera_tocar(canal):
    while canal.get_busy():
        pass


def musica_certa():
    global certos
    s = sounds.Sound("correct.wav")
    espera_tocar(s.play())
    certos.set(certos.get() + 1)


def musica_errada():
    global errados
    s = sounds.Sound("wrong.wav")
    espera_tocar(s.play())
    errados.set(errados.get() + 1)


app = Tk()
app.title("Show de calouros")
app.geometry('300x100+200+100')
sounds = pygame.mixer
sounds.init()
certos = IntVar()
certos.set(0)
errados = IntVar()
errados.set(0)
lab = Label(app, text="Aperte os botões!", height=3)
lab.pack()
lab1 = Label(app, textvariable=certos)
lab1.pack(side='left')
lab2 = Label(app, textvariable=errados)
lab2.pack(side='right')
b1 = Button(app, text="Certo!", width=10, command=musica_certa)
b1.pack(side="left", padx=10, pady=10)
b2 = Button(app, text="Errado!", width=10, command=musica_errada)
b2.pack(side="right", padx=10, pady=10)
app.mainloop()
