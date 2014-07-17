from Tkinter import *
import math
import Image 
import ImageTk
import cv2
import cv2.cv as cv
import numpy as np

root = Tk()

class Main:

	def __init__(self, raw_):
		self.raw_ = raw_
		raw_.bind("<Button-1>", self.point_One)

	def point_One(self, event):
		self.x1, self.y1 = (event.x - 1), (event.y - 1)
		self.raw_.create_oval(self.x1 - 2, self.y1 - 2, self.x1 + 2, self.y1 + 2, fill = 'green')
		raw_.bind("<Button-1>", self.point_Two)

	def point_Two(self, event):
		self.x2, self.y2 = (event.x - 1), (event.y - 1)
		self.raw_.create_oval(self.x2 - 2, self.y2 - 2, self.x2 + 2, self.y2 + 2, fill = 'green')
		raw_.bind("<Button-1>", self.point_Three)

	def point_Three(self, event):
		self.x3, self.y3 = (event.x - 1), (event.y - 1)
		self.raw_.create_oval(self.x3 - 2, self.y3 - 2, self.x3 + 2, self.y3 + 2, fill = 'green')
		raw_.bind("<Button-1>", self.circle_Calc)

	def circle_Calc(self, event):
		self.A = np.array([self.x1, self.y1, 0.0])
		self.B = np.array([self.x2, self.y2, 0.0])
		self.C = np.array([self.x3, self.y3, 0.0])
		self.a = np.linalg.norm(self.C - self.B)
		self.b = np.linalg.norm(self.C - self.A)
		self.c = np.linalg.norm(self.B - self.A)
		self.s = (self.a + self.b + self.c) / 2
		self.R = self.a*self.b*self.c / 4 / np.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))
		self.b1 = self.a*self.a * (self.b*self.b + self.c*self.c - self.a*self.a)
		self.b2 = self.b*self.b * (self.a*self.a + self.c*self.c - self.b*self.b)
		self.b3 = self.c*self.c * (self.a*self.a + self.b*self.b - self.c*self.c)
		self.P = np.column_stack((self.A, self.B, self.C)).dot(np.hstack((self.b1, self.b2, self.b3)))
		self.P /= self.b1 + self.b2 + self.b3

		self.raw_.create_oval(self.P[0] - self.R, self.P[1] - self.R, self.P[0] + self.R, self.P[1] + self.R, fill = "", outline = "black")
		raw_.bind("<Button-1>", self.point_One)




sample_Image = Image.open("test.png")
sample_Image1 = ImageTk.PhotoImage(sample_Image)
raw_ = Canvas(width = sample_Image.size[0] + 20 , height = sample_Image.size[1] + 20)
raw_.create_image(10, 10, anchor = NW, image = sample_Image1)
raw_.config(cursor = "cross")
raw_.pack(expand=YES, fill=BOTH)
Main(raw_,)
root.mainloop()
