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
        image1 = images(self.root, "Resourses/jarvis.jpg")
        button1 = buttons(root, "black", "white", "Task", "Arial 20", run, 5, 1000)
        Terminal = Text(root)
        Terminal.configure(background = "black", foreground = "white")
        Terminal.configure(width = 40, height = 30)
        Terminal.configure(font = ("arial", 20))
        Terminal.place(x = 5, y = 10)
        old_stdout = sys.stdout
        sys.stdout = Redirect(Terminal)
        gif1 = Gif(root, "Resourses/ironman.gif", 2000, 20)
        gif1.play_gif()
        
class labels():
    def __init__(self, root, LabelText, LabelFont, bg, w, h, xcoord, ycoord):
        self.root = root
        self.label = Label(root, text = LabelText, font = LabelFont, background = bg, width = w, height = h)
        self.label.place(x = xcoord, y = ycoord, anchor = "center")

class buttons():
    def __init__(self, root, Background, Foreground, Btext, Bfont, Bcommand, xcoord, ycoord):
        self.root = root
        self.button = Button(root, bg = Background, fg = Foreground, text = Btext, font = Bfont, command = Bcommand)
        self.button.place(x = xcoord, y = ycoord)

class images():
    def __init__(self, root, path):
        self.root = root
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.label = Label(root, image = self.img)
        self.label.image = self.img
        self.label.pack(fill = "both", expand = True)

class Gif():
    def __init__(self, root, gif_name, xcoords, ycoords):
        self.root = root
        self.gif_name = gif_name
        self.xcoords = xcoords
        self.ycoords = ycoords

    def play_gif(self):
        global gifimg
        gifimg = Image.open(self.gif_name)
        giflbl = Label(self.root)
        giflbl.place(x = self.xcoords, y = self.ycoords)
        
        for gifimg in ImageSequence.Iterator(gifimg):
            gifimg = ImageTk.PhotoImage(gifimg)
            giflbl.configure(image = gifimg)
            self.root.update()
            time.sleep(0.02)

        self.root.after(500, lambda : Gif.play_gif(self))

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
        self.root = root
        self.text = Text(root, background = bg, foreground = fg, width = w, height = h, font = f)
        self.text.place(x = xcoord, y = ycoord)

def task():
    time.sleep(1)
    print(pyautogui.position())

def run():
    threading.Thread(target = task).start()

def main():
    root = Tk()
    Jarvis = JarvisGUI(root)

    root.mainloop()

if __name__ == '__main__':
    main()
