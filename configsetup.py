#! /usr/bin/env python
import json
from tkinter import *
from tkinter import messagebox


class Configwindow:
    def __init__(self, win):
        self.xl = 30
        self.yl = 50
        self.xe = 160
        self.ye = 50
        self.font = ('courier', 10, 'bold')
        self.lbl1 = Label(win, text='Token', font=self.font)
        self.lbl2 = Label(win, text='Prefix', font=self.font)
        self.lbl3 = Label(win, text='Guild ID', font=self.font)
        self.lbl4 = Label(win, text='Admin Role ID', font=self.font)
        self.b1 = Button(win, text='Submit', command=self.write)
        self.t1 = Entry(font=self.font)
        self.t2 = Entry(font=self.font)
        self.t3 = Entry(font=self.font)
        self.t4 = Entry(font=self.font)
        entries = [self.t1, self.t2, self.t3, self.t4]
        for entry in entries:
            entry.place(x=self.xe, y=self.ye)
            self.ye += 50

        labels = [self.lbl1, self.lbl2, self.lbl3, self.lbl4]
        for label in labels:
            label.place(x=self.xl, y=self.yl)
            self.yl += 50

        self.b1.place(x=200, y=250, anchor=CENTER)

    def write(self):
        if self.t1.get() != '' or self.t2.get() != '' or self.t3.get() != '' or self.t4.get() != '':
            with open("config.json", "r+") as file:
                config = json.load(file)
                config["token"] = self.t1.get()
                config["prefix"] = self.t2.get()
                config["guild"] = int(self.t3.get())
                config["admin"] = int(self.t4.get())
                file.seek(0)
                json.dump(config, file, indent=4)
                file.truncate()
                messagebox.showinfo("Success", "Config file updated")
                exit()
        else:
            self.warning = messagebox.showwarning(
                title="Error", message="Please fill in all fields")


window = Tk()
window.resizable(False, False)
mywin = Configwindow(window)
window.title('Config')
window.geometry("380x300+10+10")
window.mainloop()
