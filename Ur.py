import datetime
from tkinter import *
from math import *
RATE = 1000
SIZE = 800, 600
centrum = SIZE[0]/2, SIZE[1]/2
radius = 200
sizeBigTick = radius * 4/5
sizeSmallTick = radius * 9/10
sizeHourPoint = radius * 6/10
sizeMinutesPoint = radius * 9/10
sizeSecondsPoint = radius
backgroundColor = '#FFF'
watchColor = '#FFF'

def updateTask(root, canvas):
    canvas.delete(ALL)
    t = datetime.datetime.now()
    tNow = str(t.hour) + ':' + str(t.minute) + ':' +str(t.second)
    print(tNow)
    DrawDigitalWatch(canvas)
    canvas.create_oval(centrum [0]-radius, centrum [1]-radius, centrum [0]+radius, centrum [1]+radius, width=2, fill=watchColor)
    drawTicks(canvas)
    root.after(RATE, updateTask, root, canvas)
    pointer(canvas, t)


def main():
    root = Tk()
    root.title("Ur")
    root.geometry(str(SIZE[0]) + 'x' + str(SIZE[1]))
    canvas = Canvas(width=SIZE[0], height=SIZE[1], bg=backgroundColor)
    canvas.pack(expand=YES, fill=BOTH)
    updateTask(root, canvas)
    root.mainloop()

def drawTicks(canvas):
    for h in range(1, 13):
        p = h/12
        rad = p * 2 * pi
        x=radius * cos(rad)
        y=radius * sin(rad)
        subtX= sizeBigTick * cos(rad)
        subtY= sizeBigTick * sin(rad)
        canvas.create_line(centrum[0] + subtX,centrum [1] + subtY, x + centrum[0], y + centrum[1], width=8, fill='black')

    for s in range(1, 61):
        p = s/60
        rad = p * 2 * pi
        x=radius * cos(rad)
        y=radius * sin(rad)
        subtX= sizeSmallTick * cos(rad)
        subtY= sizeSmallTick * sin(rad)
        canvas.create_line(centrum[0] + subtX,centrum [1] + subtY, x + centrum[0], y + centrum[1], width=1, fill='black')

def pointer(canvas, t):
    klok=t.hour
    minu = t.minute
    sec = t.second

    rad = (klok * (1/12) + minu * (1 / 720)) *2*pi-1/2*pi
    x = cos(rad)* sizeHourPoint
    y = sin(rad)* sizeHourPoint
    canvas.create_line(centrum [0], centrum [1], x+centrum[0], y+centrum[1], width=10, fill='black')

    rad = minu * (1 / 60) * 2 * pi-1/2*pi
    x = cos(rad) * sizeMinutesPoint
    y = sin(rad) * sizeMinutesPoint
    canvas.create_line(centrum[0], centrum[1], x + centrum[0], y + centrum[1], width=4, fill='black')

    rad = sec*(1 / 60)*2*pi-1/2*pi
    x = cos(rad) * sizeSecondsPoint
    y = sin(rad) * sizeSecondsPoint
    canvas.create_line(centrum [0], centrum [1], x+centrum[0], y+centrum[1], width=2, fill='red')

def DrawDigitalWatch(canvas):
    t = datetime.datetime.now()
    tNow = str(t.hour) + ':' + str(t.minute) + ':' + str(t.second)
    canvas.create_rectangle(centrum [0]-radius, 0,centrum [0]+radius, centrum [1]-radius-10, fill='black')
    canvas.create_text(centrum [0]-radius, 0, font=('',65), text=tNow, anchor='nw', fill='#00ABD3')



main()
