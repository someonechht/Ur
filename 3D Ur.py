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
sizeMinutesPoint = radius*3/4
sizeSecondsPoint = 3/4
backgroundColor = '#FFF'
watchColor = '#FFF'
hourText = 0
secDiscRadius = radius*(1/2)
minDiscRadius = radius*(3/4)
hourDiscRadius = radius

def updateTask(root, canvas):
    canvas.delete(ALL)
    t = datetime.datetime.now()
    tNow = str(t.hour) + ':' + str(t.minute) + ':' +str(t.second)
    secRotation = cos((t.second + t.microsecond / 1000000)*(1 / 60) * 2 * pi - 1 / 2 * pi) * secDiscRadius
    minRotation = sin((t.second + t.microsecond / 1000000)*(1 / 60) * 2 * pi - 1 / 2 * pi) * minDiscRadius
    hourRotation = tan((t.second + t.microsecond / 1000000) * (1 / 60) * 2 * pi - 1 / 2 * pi) * hourDiscRadius

#    drawDigitalWatch(canvas, t)
    drawSecDisc(canvas, t, secRotation)
    drawMinDisc(canvas, t, minRotation)
    drawHourDisc(canvas, t, hourRotation, hourText)
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
    hourText = 0
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
    sec = t.second #time in sec
    canvas.create_oval(centrum[0] - secRotation, centrum[1] - secDiscRadius, centrum[0] + secRotation, centrum[1] + secDiscRadius, width=2)

    for i in range(1, 61):
        # Small ticks
        rotation = sec / 60 * 2 * pi
        p = i/60
        rad = p * 2 * pi+rotation
        x= secRotation * cos(rad)
        y=secDiscRadius * sin(rad)
        canvas.create_line(centrum[0]+sizeSmallTick*x, centrum [1]+sizeSmallTick*y, x + centrum[0], y + centrum[1], width=1)

        # disc text
        canvas.create_text(x + centrum[0] + x / 10, y + centrum[1] + y / 10, text=60 - i)

        # Big ticks
        p = i/12
        rad = p * 2 * pi+rotation
        x= secRotation * cos(rad)
        y=secDiscRadius * sin(rad)
        canvas.create_line(centrum[0]+sizeSecondsPoint*x, centrum [1]+sizeSecondsPoint*y, x + centrum[0], y + centrum[1], width=1)

def drawMinDisc(canvas, t, minRotation):
    min = t.minute #time in min
    canvas.create_oval(centrum[0] - minRotation, centrum[1] - minDiscRadius, centrum[0] + minRotation, centrum[1] + minDiscRadius, width=4)


    for i in range(1, 61):
        #Small ticks
        p = i/60
        rad = p * 2 * pi
        x=minRotation * cos(rad)
        y=minDiscRadius * sin(rad)
        canvas.create_line(centrum[0]+sizeSmallTick*x, centrum [1]+sizeSmallTick*y, x + centrum[0], y + centrum[1], width=2)
        #disc text
        canvas.create_text(x + centrum[0] + x / 10, y + centrum[1] + y / 10, text=60 - i)
        # Big ticks
        rotation = min / 60 * 2 * pi
        p = i / 12
        rad = p * 2 * pi + rotation
        x = minRotation * cos(rad)
        y = minDiscRadius * sin(rad)
        canvas.create_line(centrum[0] + sizeSecondsPoint * x, centrum[1] + sizeSecondsPoint * y, x + centrum[0],y + centrum[1], width=2)

def drawHourDisc(canvas, t, hourRotation, hourText):
    hour = t.second #time in hours
    canvas.create_oval(centrum[0] - hourRotation, centrum[1] - radius, centrum[0] + hourRotation, centrum[1] + radius, width=4)

    for i in range(1, 61):
        #Small ticks
        rad = i/60 * 2 * pi
        x= hourRotation * cos(rad)
        y=radius * sin(rad)
        canvas.create_line(centrum[0]+sizeSmallTick*x, centrum [1]+sizeSmallTick*y, x + centrum[0], y + centrum[1], width=2)
        # Big ticks
        rotation = hour / 60 * 2 * pi
        rad = i/12 * 2 * pi + rotation
        x = hourRotation * cos(rad)
        y = radius * sin(rad)
        canvas.create_line(centrum[0] + sizeSecondsPoint * x, centrum[1] + sizeSecondsPoint * y, x + centrum[0],y + centrum[1], width=2)
        # disc text
    for h in range(1, 13):
        rad = h/12 * 2* pi + rotation
        x = hourRotation * cos(rad)
        y = radius * sin(rad)
        hourText = hourText + 1
        canvas.create_text(x + centrum[0] + x / 10, y + centrum[1] + y / 10, text=12-h)

def drawDigitalWatch(canvas, t):
    tNow = t.strftime("%H:%M:%S")
    canvas.create_rectangle(centrum [0]-radius, 0,centrum [0]+radius, centrum [1]-radius-10, fill='black')
    canvas.create_text(centrum [0]-radius, 0, font=('',65), text=tNow, anchor='nw', fill='#00ABD3')



main()
