
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import src.gui as gui



#function test
# def donothing():
# 	print("do nothingggg")
#function test of gui file chain
# print(gui.dodonothing())



root = Tk()
root.title("HelloRobo")
root.minsize(800,500)
root.geometry("1200x500")

gui = gui.Gui(root)

# gui.init_menu()
gui.init_control_frame()
gui.init_status_frame()

root.mainloop()




