#4/4

from tkinter import *

class Face:

    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter Face")
        self.frame = Frame(master)
        self.canvas = Canvas(master, width = 400, height = 500)
        self.canvas.pack()
        self.create_ears()
        self.create_faceOutline()
        self.create_eyes()
        self.create_nose()
        self.create_mouth()

    def create_faceOutline(self):

        self.face = self.canvas.create_oval(100,100, 300, 400,fill='bisque')

    def create_eyes(self):

        self.leye = [self.canvas.create_oval(130, 162.5, 170, 237.5, fill='white'), \
                     self.canvas.create_oval(145,200,155,220, fill='black')]
        self.reye = [self.canvas.create_oval(230, 162.5, 270, 237.5, fill='white'), \
                     self.canvas.create_oval(245,200,255,220, fill='black')]

    def create_nose(self):

        self.nose = self.canvas.create_polygon(200,250,185,300,215,300,
                                               outline='black',
                                               fill='')

    def create_ears(self):
        
        self.lears = [self.canvas.create_oval(80,212.5,120,287.5, fill='bisque'), \
                     self.canvas.create_oval(90,222.5,110,277.5), \
                     self.canvas.create_oval(95,245,105,260)]
        
        self.rears = [self.canvas.create_oval(280,212.5,320,287.5, fill='bisque'), \
                     self.canvas.create_oval(290,222.5,310,277.5), \
                     self.canvas.create_oval(295,245,305,260)]
        
    def create_mouth(self):

        self.mouth = [self.canvas.create_oval(175,301,225,360, fill='black'), \
                      self.canvas.create_rectangle(150,301,250,325, outline='',
                                                   fill='bisque')]

root = Tk()
App = Face(root)
root.mainloop()
