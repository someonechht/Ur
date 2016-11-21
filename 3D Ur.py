# asdf
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
sizeSmallTick = radius * 9/10
sizeHourPoint = radius * 1/2
sizeMinutesPoint = radius*  3/4
sizeSecondsPoint = radius/2
backgroundColor = '#FFF'
watchColor = '#FFF'
widtht = radius*2

def updateTask(root, canvas):
    canvas.delete(ALL)
    t = datetime.datetime.now()
    tNow = str(t.hour) + ':' + str(t.minute) + ':' +str(t.second)
    print(t)
    drawDigitalWatch(canvas, t)
    drawSecDisc(canvas, t)
    drawMinDisc(canvas, t)
    root.after(1000 - t.microsecond // 1000, updateTask, root, canvas)
    pointer(canvas, t)
    drawDaOval(canvas, t)

def convertDimension(q, w, e, r):
    x=q/r
    y=w/r
    z=e/r
    u = x / z
    v = y / z
    return u, v

def drawDaOval(canvas, t):
    global widtht
    sec = t.second
    rad = sec*(1 / 60)*2*pi-1/2*pi

    60/(2*pi)
    widtht = cos(rad)*200
    z = sin(rad)





def main():
    root = Tk()
    root.title("Ur")
    root.geometry(str(SIZE[0]) + 'x' + str(SIZE[1]))
    canvas = Canvas(width=SIZE[0], height=SIZE[1], bg=backgroundColor)
    canvas.pack(expand=YES, fill=BOTH)
    updateTask(root, canvas)
    root.mainloop()

def pointer(canvas, t):
    canvas.create_line(centrum [0], centrum [1], centrum[0], centrum[1]-radius, width=2, fill='red')

def drawSecDisc(canvas, t):
    sec = t.second
    canvas.create_oval(centrum[0]-widtht , centrum[1] - radius, centrum[0] + widtht, centrum[1] + radius, width=2)
    for h in range(1, 13):
        rotation = sec/60*2*pi
        p = h/12
        rad = p * 2 * pi+rotation
        x=radius * cos(rad)
        y=radius * sin(rad)
        subtX= sizeSecondsPoint * cos(rad)
        subtY= sizeSecondsPoint * sin(rad)
        canvas.create_line(centrum[0] + subtX,centrum [1] + subtY, x + centrum[0], y + centrum[1], width=1, fill='black')

    for s in range(1, 61):
        p = s/60
        rad = p * 2 * pi
        x=radius * cos(rad)
        y=radius * sin(rad)
        z=radius * (rad)
        subtX= (sizeSmallTick * cos(rad))
        subtY= (sizeSmallTick * sin(rad))
        canvas.create_line(centrum[0] + subtX,centrum [1] + subtY, x + centrum[0], y + centrum[1], width=1, fill='black')

def drawMinDisc(canvas, t):
    minu = t.minute
    canvas.create_oval(centrum[0] - radius, centrum[1] - radius, centrum[0] + radius, centrum[1] + radius, width=2)
    for i in range(1, 61):
        rotation = minu / 60 * 2 * pi
        p = i / 12
        rad = p * 2 * pi + rotation
        etE = 1
        etW = radius * sin(rad)
        etQ = radius * cos(rad)
        etR = 1
        u = convertDimension(etQ, etW, etE, etR)[0]
        v = convertDimension(etQ, etW, etE, etR)[1]

        tickX = sizeMinutesPoint * cos(rad)
        tickY = sizeMinutesPoint * sin(rad)

        canvas.create_line(centrum[0] + tickX, centrum[1] + tickY, u + centrum[0], v + centrum[1], width=4, fill='black')

    for j in range(1, 61):
        p = j/60
        rad = p * 2 * pi

        etQ=radius * cos(rad)
        etW=radius * sin(rad)
        eqE=radius * (rad)
        etR=1

        u = convertDimension(etQ, etW, etE, etR)[0]
        v = convertDimension(etQ, etW, etE, etR)[1]

        subtX= (sizeSmallTick * cos(rad))
        subtY= (sizeSmallTick * sin(rad))
        canvas.create_line(centrum[0] + subtX,centrum [1] + subtY, u + centrum[0], v + centrum[1], width=2, fill='black')

def drawDigitalWatch(canvas, t):
    tNow = t.strftime("%H:%M:%S")
    canvas.create_rectangle(centrum [0]-radius, 0,centrum [0]+radius, centrum [1]-radius-10, fill='black')
    canvas.create_text(centrum [0]-radius, 0, font=('',65), text=tNow, anchor='nw', fill='#00ABD3')



main()
