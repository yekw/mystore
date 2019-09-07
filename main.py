from tkinter import *
from LoginPage import *
import pymysql


root = Tk()
root.title('图书管理')

# photo = PhotoImage(file="pic1.png")
# theLabel = Label(root,text="我是内容,\n请你阅读",justify=LEFT,image=photo,compound = CENTER,font=("华文行楷",20),fg = "white")
# theLabel.pack()
canvas = Canvas(root, width=720, height=300)
canvas.pack()
img_one = PhotoImage(file="pict.gif")
canvas.create_image(0,0,anchor=NW,image=img_one)

LoginPage(root)
root.mainloop()
