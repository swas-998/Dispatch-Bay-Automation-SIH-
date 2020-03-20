from tkinter import *

class Report:
    def top1(self):
        self.first=Toplevel()
        self.sw1 = self.first.winfo_screenwidth()
        self.sh1 = self.first.winfo_screenheight()
        self.first.geometry("%dx%d+0+0" % (self.sw1, self.sh1))
        self.first.minsize(self.sw1, self.sh1)
        self.first.title('Mannual mode')
        self.canvas = Canvas(self.first, height=self.sh1, width=self.sw1, bg='white')
        self.canvas.pack()
        Label(self.canvas,text='GOOD TAG',font=20).place(x=self.sw1/8,y=self.sh1/11)
        self.gt=Entry(self.canvas).place(x=self.sw1/5,y=self.sh1/11)
        #self.ok=Button(self.canvas,text='OK',command=self.ok_work)

        self.a = self.canvas.create_rectangle(self.sw1 /1.6,self.sw1 /20.69, self.sw1 /1.28,self.sw1/2.4, width=3)
        Label(self.canvas, text='GOOD INFORMATION', font=2).place(x=self.sw1/1.56, y=self.sh1 /11.28)


        self.first.mainloop()
    def __init__(self, window):
        self.root = window
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (self.sw, self.sh))
        self.root.minsize(self.sw, self.sh)
        self.root.title('report')
        self.w=Button(self.root, text="REPORT",bg='red',command=self.top1).place(x=self.sw-100,y=self.sh-100)
        self.root.mainloop()


if __name__ == '__main__':
    window=Tk()
    ob=Report(window)