import datetime
from tkinter import *
from math import *
RATE = 1000
SIZE = 800, 600
centrum= SIZE [0]/2, SIZE [1]/2
radius = 200

def updateTask(root, canvas):
    canvas.delete(ALL)
    t = datetime.datetime.now()
    print(t)
    drawTicks(canvas)
    canvas.create_oval(centrum [0]-radius, centrum [1]-radius, centrum [0]+radius, centrum [1]+radius, width=2, fill='')
    root.after(RATE, updateTask, root, canvas)
    pointer(canvas, t)


def main():

    root = Tk()
    root.title("Min applikation")
    root.geometry(str(SIZE[0]) + 'x' + str(SIZE[1]))
    canvas = Canvas(width=SIZE[0], height=SIZE[1], bg='white')
    canvas.pack(expand=YES, fill=BOTH)
    updateTask(root, canvas)
    root.mainloop()

def drawTicks(canvas):
    for sTick in range(1, 13):
        p = sTick/12
        rad = p * 2*pi
        x=200 * cos(rad)
        y=200 * sin(rad)
        canvas.create_line(centrum [0], centrum [1], x+centrum[0], y+centrum[1], width=5, fill='black')

def pointer(canvas, t):

    klok=t.hour

    rad = klok*(1/12)*2*pi
    x=200 * cos(rad)
    y=200 * sin(rad)
    canvas.create_line(centrum [0], centrum [1], x+centrum[0], y+centrum[1], width=20, fill='black')






main()
