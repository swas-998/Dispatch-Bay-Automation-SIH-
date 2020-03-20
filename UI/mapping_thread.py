# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:04:23 2019

@author: DELL
"""

from tkinter import *

class Maps:
     def __init__(self,window):
        self.root=window
        self.scr_width = self.root.winfo_screenwidth()
        self.scr_height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (self.scr_width,self.scr_height))
        self.root.minsize(self.scr_width,self.scr_height)
        self.root.title('mapping')
        self.x=IntVar()
        
     def back_map(self):   
        self.back=Canvas(self.root,height=self.scr_height,width=self.scr_width,bg='white')
        self.back.pack()
        self.a =self.back.create_rectangle(35,35,650,350,width=3)
        
        pos = [(60,60,175,130),(210, 60, 325, 130),(360,60,475,130),(510,60,625,130), (60,160,175,230),(210,160,325,230),(360,160,475,230),(510,160,625,230),  (60,260,175,330),(210,260,325,330),(360,260,475,330),(510,260,625,330)]
        self.rectangles = [None for _ in range(12)]
        for idx in range(12):
            self.rectangles[idx] = self.back.create_rectangle(*pos[idx], fill='white')
        
        pos=[(40,140,115,150),(115,140,185,150),(185,140,195,150)  ,(195,140,270,150),(270,140,335,150),(335,140,345,150)  ,(345,140,420,150),(420,140,490,150),(490,140,500,150)  ,(500,140,575,150)]    
        self.row1 = [None for _ in range(10)]
        for idx in range(10):
            self.row1[idx] = self.back.create_rectangle(*pos[idx], fill='white',width=0)    
        pos=[(40,240,115,250),(115,240,185,250),(185,240,195,250)  ,(195,240,270,250),(270,240,335,250),(335,240,345,250)  ,(345,240,420,250),(420,240,490,250),(490,240,500,250)  ,(500,240,575,250)]    
        self.row2= [None for _ in range(10)]
        for idx in range(10):
            self.row2[idx] = self.back.create_rectangle(*pos[idx], fill='white',width=0)
        pos=[(185,150,195,240),(335,150,345,240),(490,150,500,240)]
        self.col= [None for _ in range(3)]
        for idx in range(3):
            self.col[idx] = self.back.create_rectangle(*pos[idx], fill='white',width=0)
        self.ball=self.back.create_oval(40,140,50,150,fill='red',width=2)

     def moov(self):
          r=int(input('enter row no'))
          c=int(input('enter column no'))
          self.back.move(self.ball,r,c)
          self.root.update()
         
     def m(self,y): 
        self.x=y
        ob.back_map()
        if self.x=='A' or self.x=='E':
            self.back.itemconfig(self.row1[0], fill='green')
            if self.x=='A':
                self.back.itemconfig(self.rectangles[0], fill='red')
            else:
                self.back.itemconfig(self.rectangles[4], fill='red')
            
        if self.x=='B' or self.x=='F':
            for i in range (4):
                self.back.itemconfig(self.row1[i], fill='green')
            if self.x=='B':
                self.back.itemconfig(self.rectangles[1], fill='red')
            else:
                self.back.itemconfig(self.rectangles[5], fill='red')
           
        if self.x=='C' or self.x=='G':
            for i in range (7):
                self.back.itemconfig(self.row1[i], fill='green')
            if self.x=='C':
                self.back.itemconfig(self.rectangles[2], fill='red')
            else:
                self.back.itemconfig(self.rectangles[6], fill='red')
           
        if self.x=='D' or self.x=='H':
            for i in range (10):
                self.back.itemconfig(self.row1[i], fill='green')
            if self.x=='D':
                self.back.itemconfig(self.rectangles[3], fill='red')
            else:
                self.back.itemconfig(self.rectangles[7], fill='red')
            
             
        if self.x=='I' or self.x=='J':
            for i in range (3):
                self.back.itemconfig(self.row1[i], fill='green')
            self.back.itemconfig(self.col[0], fill='green')
            self.back.itemconfig(self.row2[2], fill='green')
            if self.x=='I':
                self.back.itemconfig(self.row2[1], fill='green')
                self.back.itemconfig(self.rectangles[8], fill='red')
            else:
                self.back.itemconfig(self.row2[3], fill='green')
                self.back.itemconfig(self.rectangles[9], fill='red')
        
        if self.x=='K' :
            for i in range (6):
                self.back.itemconfig(self.row1[i], fill='green')
            self.back.itemconfig(self.col[1], fill='green')
            self.back.itemconfig(self.row2[5], fill='green')
            self.back.itemconfig(self.row2[6], fill='green')
            self.back.itemconfig(self.rectangles[10], fill='red')
            
        if self.x=='L' :
            for i in range (9):
                self.back.itemconfig(self.row1[i], fill='green')
            self.back.itemconfig(self.col[2], fill='green')
            self.back.itemconfig(self.row2[8], fill='green')
            self.back.itemconfig(self.row2[9], fill='green')
            self.back.itemconfig(self.rectangles[11], fill='red')
        self.root.update()
          
if __name__=="__main__":
    window=Tk()
    ob=Maps(window)
    c=input("enter the grid no \n")
    ob.m(c)
    while True:
         ob.moov()
    

