import datetime
from tkinter import *
from math import *

RATE = 1000
SIZE = 800, 600

def updateTask(root, canvas):
    canvas.delete(ALL)
    t = datetime.datetime.now()
    print(t)
    canvas.create_oval(25, 25, 80, 60, width=2, fill='')
    canvas.create_line(25, 25, 80, 60, width=5, fill='black')
    root.after(RATE, updateTask, root, canvas)


def main():
    root = Tk()
    root.title("Min applikation")
    root.geometry(str(SIZE[0]) + 'x' + str(SIZE[1]))

    canvas = Canvas(width=SIZE[0], height=SIZE[1], bg='white')
    canvas.pack(expand=YES, fill=BOTH)

    updateTask(root, canvas)
    root.mainloop()


main()
