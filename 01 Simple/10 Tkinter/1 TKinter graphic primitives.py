from tkinter import *
root = Tk()

class point():
    def __init__(self):
        self.x = 0
        self.y = 0
    def setxy(self,x,y):
        if x > 590:
            self.x = 590
        elif x < 10:
            self.x = 10
        else:
            self.x = x
        if y > 590:
            self.y = 590
        elif y < 10:
            self.y = 10
        else:
            self.y = y
    def addpoint(self,canvas):
        x1 = self.x + 10
        y1 = self.y + 10
        canvas.c.create_oval(self.x,self.y,x1,y1, fill='grey70', outline='white', width=2)

class line():
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
    def setxy1(self,x,y):
        if x > 590:
            self.x1 = 590
        elif x < 10:
            self.x1 = 10
        else:
            self.x1 = x
        if y > 590:
            self.y1 = 590
        elif y < 10:
            self.y1 = 10
        else:
            self.y1 = y
    def setxy2(self,x,y):
        if x > 590:
            self.x2 = 590
        elif x < 10:
            self.x2 = 10
        else:
            self.x2 = x
        if y > 590:
            self.y2 = 590
        elif y < 10:
            self.y2 = 10
        else:
            self.y2 = y
    def addline(self,canvas):
        canvas.c.create_line(self.x1,self.y1,self.x2,self.y2)

class rectangle():
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
    def setxy1(self,x,y):
        if x > 590:
            self.x1 = 590
        elif x < 10:
            self.x1 = 10
        else:
            self.x1 = x
        if y > 590:
            self.y1 = 590
        elif y < 10:
            self.y1 = 10
        else:
            self.y1 = y
    def setxy2(self,x,y):
        if x > 590:
            self.x2 = 590
        elif x < 10:
            self.x2 = 10
        else:
            self.x2 = x
        if y > 590:
            self.y2 = 590
        elif y < 10:
            self.y2 = 10
        else:
            self.y2 = y
    def addrect(self, canvas):
        canvas.c.create_rectangle(self.x1,self.y1,self.x2,self.y2)

class circ():
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
    def setxy1(self, x, y):
        if x > 590:
            self.x1 = 590
        elif x < 10:
            self.x1 = 10
        else:
            self.x1 = x
        if y > 590:
            self.y1 = 590
        elif y < 10:
            self.y1 = 10
        else:
            self.y1 = y
    def setxy2(self, x, y):
        if x > 590:
            self.x2 = 590
        elif x < 10:
            self.x2 = 10
        else:
            self.x2 = x
        if y > 590:
            self.y2 = 590
        elif y < 10:
            self.y2 = 10
        else:
            self.y2 = y
    def addcirc(self, canvas):
        canvas.c.create_oval(self.x1, self.y1, self.x2, self.y2)


class canvas():
    def __init__(self):
        self.c = Canvas(root, width=600, height=600, bg='white')
        self.c.pack()

canvases = []
points = []
lines = []
rects = []
circs = []

def click1():
    global txt1,txt2,txt3,txt4,txt5,txt6,points,canvases
    x = txt1.get()
    y = txt2.get()
    new_point = point()
    new_point.setxy(int(x),int(y))
    new_point.addpoint(canvases[0])
    points.append(new_point)
def click2():
    global txt3,txt4,txt5,txt6,lines,canvases
    x1 = txt3.get()
    y1 = txt4.get()
    x2 = txt5.get()
    y2 = txt6.get()
    new_line = line()
    new_line.setxy1(int(x1),int(y1))
    new_line.setxy2(int(x2), int(y2))
    new_line.addline(canvases[0])
    lines.append(new_line)
def click3():
    global txt3,txt4,txt5,txt6,rects,canvases
    x1 = txt3.get()
    y1 = txt4.get()
    x2 = txt5.get()
    y2 = txt6.get()
    new_rect = rectangle()
    new_rect.setxy1(int(x1),int(y1))
    new_rect.setxy2(int(x2), int(y2))
    new_rect.addrect(canvases[0])
    rects.append(new_rect)
def click4():
    global txt3,txt4,txt5,txt6,circs,canvases
    x1 = txt3.get()
    y1 = txt4.get()
    x2 = txt5.get()
    y2 = txt6.get()
    new_circ = circ()
    new_circ.setxy1(int(x1),int(y1))
    new_circ.setxy2(int(x2), int(y2))
    new_circ.addcirc(canvases[0])
    circs.append(new_circ)
def main():
    global txt1,txt2,txt3,txt4,txt5,txt6,new_canvas
    root = Tk()
    new_canvas = canvas()
    canvases.append(new_canvas)
    root.geometry("800x250")
    lbl1 = Label(root, text="x(10-590)=", font=("Arial Bold", 10))
    lbl1.grid(column=2, row=0)
    txt1 = Entry(root, width=10)
    txt1.grid(column=3, row=0)
    lbl2 = Label(root, text="y(10-590)=", font=("Arial Bold", 10))
    lbl2.grid(column=4, row=0)
    txt2 = Entry(root, width=10)
    txt2.grid(column=5, row=0)
    btn1 = Button(root, text="Добавить точку", command=click1)
    btn1.grid(column=1, row=0)

    lbl3 = Label(root, text="x1(10-590)=", font=("Arial Bold", 10))
    lbl3.grid(column=2, row=1)
    txt3 = Entry(root, width=10)
    txt3.grid(column=3, row=1)
    lbl4 = Label(root, text="y1(10-590)=", font=("Arial Bold", 10))
    lbl4.grid(column=4, row=1)
    txt4 = Entry(root, width=10)
    txt4.grid(column=5, row=1)
    lbl5 = Label(root, text="x2(10-590)=", font=("Arial Bold", 10))
    lbl5.grid(column=6, row=1)
    txt5 = Entry(root, width=10)
    txt5.grid(column=7, row=1)
    lbl6 = Label(root, text="y2(10-590)=", font=("Arial Bold", 10))
    lbl6.grid(column=8, row=1)
    txt6 = Entry(root, width=10)
    txt6.grid(column=9, row=1)
    btn2 = Button(root, text="Добавить линию", command=click2)
    btn2.grid(column=1, row=1)
    btn3 = Button(root, text="Добавить прямоугольник", command=click3)
    btn3.grid(column=1, row=2)
    btn4 = Button(root, text="Добавить овал", command=click4)
    btn4.grid(column=2, row=2)

    root.mainloop()

if __name__ == '__main__':
    main()
