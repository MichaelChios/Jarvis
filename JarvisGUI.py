from tkinter import *
import threading
import sys
from Jarvis import *
from PIL import ImageTk, Image, ImageSequence
import pyautogui
import time

class JarvisGUI():
    def __init__(self, root):
        self.root = root
        self.WinHeight = root.winfo_screenheight()
        self.WinWidth = root.winfo_screenwidth()
        self.root.geometry(f"{self.WinWidth}x{self.WinHeight}+0+0")
        self.root.configure(background = "blue")
        image1 = images(self.root, "jarvis.jpg")
        button1 = buttons(root, "black", "white", "Button", "Arial 20", task, 5, 1000)
        
class labels():
    def __init__(self, root, LabelText, LabelFont, bg, w, h, xcoord, ycoord):
        self.label = Label(root, text = LabelText, font = LabelFont, background = bg, width = w, height = h)
        self.label.place(x = xcoord, y = ycoord, anchor = "center")

class buttons():
    def __init__(self, root, Background, Foreground, Btext, Bfont, Bcommand, xcoord, ycoord):
        self.button = Button(root, bg = Background, fg = Foreground, text = Btext, font = Bfont, command = Bcommand)
        self.button.place(x = xcoord, y = ycoord)

class images():
    def __init__(self, root, path):
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.label = Label(root, image = self.img)
        self.label.image = self.img
        self.label.pack(fill = "both", expand = True)

class Redirect():
    def __init__(self, widget, autoscroll = True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        if (self.autoscroll == True):
            self.widget.see('end')

class textWidget():
    def __init__(self, root, bg, fg, w, h, f, xcoord, ycoord):
        self.text = Text(root, background = bg, foreground = fg, width = w, height = h, font = f)
        self.text.place(x = xcoord, y = ycoord)

def task():
    time.sleep(5)
    print(pyautogui.position())

root = Tk()
Jarvis = JarvisGUI(root)
Terminal = Text(root)
Terminal.configure(background = "black", foreground = "white")
Terminal.configure(width = 40, height = 30)
Terminal.configure(font = ("arial", 20))
Terminal.place(x = 5, y = 10)
old_stdout = sys.stdout
sys.stdout = Redirect(Terminal)

root.mainloop()
