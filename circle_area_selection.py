from Tkinter import *
import math
import Image 
import ImageTk

root = Tk()

class Main:

	def __init__(self, raw_):
		self.raw_ = raw_
		raw_.bind("<Button-1>", self.center)

	def center(self,event):
		self.x1, self.y1 = (event.x - 1), (event.y - 1)
		self.raw_.create_rectangle(self.x1 + 2,self.y1 + 2,self.x1 - 2,self.y1 - 2,fill='red')
		raw_.bind("<Button-1>", self.outer_Circle)

	def outer_Circle(self,event):
		self.oc_x, self.oc_y = (event.x + 1), (event.y + 1)
		self.r1 = math.sqrt(((self.oc_x - self.x1) ** 2) + ((self.oc_y - self.y1) ** 2))
		self.raw_.create_oval(self.x1 - self.r1, self.y1 - self.r1, self.x1 + self.r1, self.y1 + self.r1, fill = "", outline = "black")
		raw_.bind("<Button-1>", self.inner_Circle)

	def inner_Circle(self,event):
		self.ic_x, self.ic_y = (event.x + 1), (event.y + 1)
		self.r2 = math.sqrt(((self.ic_x - self.x1) ** 2) + ((self.ic_y - self.y1) ** 2))
		self.raw_.create_oval(self.x1 - self.r2, self.y1 - self.r2, self.x1 + self.r2, self.y1 + self.r2, fill = "", outline = "black")
		self.pixle_Value()

	def pixle_Value(self):
		#Calculations
		print("we made it")

sample_Image = Image.open("test.png")
sample_Image1 = ImageTk.PhotoImage(sample_Image)
raw_ = Canvas(width = sample_Image.size[0] + 20 , height = sample_Image.size[1] + 20)
raw_.create_image(10, 10, anchor = NW, image = sample_Image1)
raw_.config(cursor = "cross")
raw_.pack(expand=YES, fill=BOTH)

Main(raw_)
root.mainloop()

		



