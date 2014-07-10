from Tkinter import *
import math

root=Tk()

class Handler:

    def __init__(self, w):
        self.w = w
        w.bind("<Button-1>", self.center)
        w.bind("<ButtonRelease-1>", self.create)


    def center(self, event):
        self.x1, self.y1 = (event.x - 1), (event.y - 1)

    def radius(self, event):
        self.x2, self.y2 = (event.x + 1), (event.y + 1)

    def create(self, event):
        self.radius(event)
        self.r = math.sqrt(((self.x1 - self.x2) ** 2) + ((self.y1 - self.y2) ** 2))
        self.w.create_oval(self.x1 - self.r,self.y1 - self.r ,self.x1 + self.r, self.y1 +self.r,fill='',outline="black")

w = Canvas(root, width=800, height=800)
w.config(cursor='cross')
w.pack(expand=YES, fill=BOTH)

Handler(w)
root.mainloop()