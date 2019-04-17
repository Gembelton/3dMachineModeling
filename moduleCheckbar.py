from tkinter import *


class Checkbar():
    def __init__(self, screen, checkBarName, pos):
        self.var = IntVar()
        chk = Checkbutton(screen, text=checkBarName, font="courier 10",
                          variable=self.var, command=self.var_states).grid(row=pos[0], column=pos[1])

    def var_states(self):
        return self.var.get()
