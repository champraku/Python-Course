#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

root = tkinter.Tk()
root.title('Canvas shapes')

canvas = tkinter.Canvas(root)
canvas.create_oval(10, 10, 80, 80, outline="#f11", 
    fill="#1f1", width=2)
canvas.create_oval(110, 10, 210, 80, outline="#f11", 
    fill="#1f1", width=2)
canvas.create_rectangle(230, 10, 290, 60, 
    outline="#f11", fill="#1f1", width=2)
canvas.create_arc(30, 200, 90, 100, start=0, 
    extent=210, outline="#f11", fill="#1f1", width=2)
    
points = [150, 100, 200, 120, 240, 180, 210, 
    200, 150, 150, 100, 200]
canvas.create_polygon(points, outline='#f11', 
    fill='#1f1', width=2)
canvas.pack(fill=tkinter.BOTH, expand=1)

root.geometry("330x220+300+300")
root.mainloop()
