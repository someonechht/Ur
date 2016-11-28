# http://stackoverflow.com/questions/6139451/how-can-i-convert-3d-space-coordinates-to-2d-space-coordinates
# https://matb1htx.systime.dk/?id=c891
# (q,w,e,r) 4D
# (x,y,z) 3D
# (u,v) 2D

# fra 3D til 2D
# u = x / z;
# v = y / z;

# fra 4D til 3D
# x=q/r
# y=w/r
# z=e/r

import datetime
from tkinter import *
from math import *
RATE = 1000
SIZE = 800, 600
centrum = SIZE[0]/2, SIZE[1]/2
radius = 200
sizeBigTick = radius * 4/5
sizeSmallTick = 9/10
sizeHourPoint = radius * 1/2
sizeMinutesPoint = radius*  3/4
sizeSecondsPoint = 3/4
backgroundColor = '#FFF'
watchColor = '#FFF'

def updateTask(root, canvas):
    canvas.delete(ALL)
    t = datetime.datetime.now()
    tNow = str(t.hour) + ':' + str(t.minute) + ':' +str(t.second)
    secRotation = cos((t.second + t.microsecond / 1000000)*(1 / 60) * 2 * pi - 1 / 2 * pi) * radius
    minRotation = sin((t.second + t.microsecond / 1000000)*(1 / 60) * 2 * pi - 1 / 2 * pi) * radius
    hourRotation = tan((t.second + t.microsecond / 1000000) * (1 / 60) * 2 * pi - 1 / 2 * pi) * radius

    drawDigitalWatch(canvas, t)
    drawSecDisc(canvas, t, secRotation)
    drawMinDisc(canvas, t, minRotation)
    drawHourDisc(canvas, t, hourRotation)
    pointer(canvas)

    root.after(100 - t.microsecond // 10000, updateTask, root, canvas)
def convertDimension(q,w,e,r):
    x=q/r
    y=w/r
    z=e/r
    u = x / z
    v = y / z
    return u, v

def main():
    root = Tk()
    root.title("Ur")
    root.geometry(str(SIZE[0]) + 'x' + str(SIZE[1]))
    canvas = Canvas(width=SIZE[0], height=SIZE[1], bg=backgroundColor)
    canvas.pack(expand=YES, fill=BOTH)
    updateTask(root, canvas)
    root.mainloop()

def pointer(canvas):
    canvas.create_line(centrum [0], centrum [1], centrum[0], centrum[1]-radius, width=2, fill='red')

def drawSecDisc(canvas, t, secRotation):
    sec = t.second
    canvas.create_oval(centrum[0] - secRotation, centrum[1] - radius, centrum[0] + secRotation, centrum[1] + radius, width=2)

    for h in range(1, 13):
        rotation = sec/60*2*pi
        p = h/12
        rad = p * 2 * pi+rotation
        x= secRotation * cos(rad)
        y=radius * sin(rad)
        canvas.create_line(centrum[0]+sizeSecondsPoint*x, centrum [1]+sizeSecondsPoint*y, x + centrum[0], y + centrum[1], width=1)

    for i in range(1, 61):
        p = i/60
        rad = p * 2 * pi
        x= secRotation * cos(rad)
        y=radius * sin(rad)
        canvas.create_line(centrum[0]+sizeSmallTick*x, centrum [1]+sizeSmallTick*y, x + centrum[0], y + centrum[1], width=1)

def drawMinDisc(canvas, t, minRotation):
    min = t.minute
    canvas.create_oval(centrum[0] - minRotation, centrum[1] - radius, centrum[0] + minRotation, centrum[1] + radius, width=4)

    for h in range(1, 13):
        rotation = min/60*2*pi
        p = h/12
        rad = p * 2 * pi+rotation
        x=minRotation * cos(rad)
        y=radius * sin(rad)
        canvas.create_line(centrum[0]+sizeSecondsPoint*x, centrum [1]+sizeSecondsPoint*y, x + centrum[0], y + centrum[1], width=2)

    for i in range(1, 61):
        p = i/60
        rad = p * 2 * pi
        x=minRotation * cos(rad)
        y=radius * sin(rad)
        canvas.create_line(centrum[0]+sizeSmallTick*x, centrum [1]+sizeSmallTick*y, x + centrum[0], y + centrum[1], width=2)

def drawHourDisc(canvas, t, hourRotation):
    hour = t.second
    canvas.create_oval(centrum[0] - hourRotation, centrum[1] - radius, centrum[0] + hourRotation, centrum[1] + radius, width=4)

    for h in range(1, 13):
        rotation = hour/60*2*pi
        p = h/12
        rad = p * 2 * pi+rotation
        x= hourRotation * cos(rad)
        y = radius * sin(rad)
        canvas.create_line(centrum[0]+sizeSecondsPoint*x, centrum [1]+sizeSecondsPoint*y, x + centrum[0], y + centrum[1], width=2)

    for i in range(1, 61):
        p = i/60
        rad = p * 2 * pi
        x= hourRotation * cos(rad)
        y=radius * sin(rad)
        canvas.create_line(centrum[0]+sizeSmallTick*x, centrum [1]+sizeSmallTick*y, x + centrum[0], y + centrum[1], width=2)

def drawDigitalWatch(canvas, t):
    tNow = t.strftime("%H:%M:%S")
    canvas.create_rectangle(centrum [0]-radius, 0,centrum [0]+radius, centrum [1]-radius-10, fill='black')
    canvas.create_text(centrum [0]-radius, 0, font=('',65), text=tNow, anchor='nw', fill='#00ABD3')



main()
