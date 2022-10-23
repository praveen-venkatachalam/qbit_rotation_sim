import os
import qiskit
import tkinter

#Define Window
root = tkinter.Tk()
root.title('Qbit Rotation Simulator')

#set size
root.geometry('399x410')
root.resizable(0,0)

# #Define color and fonts
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font = ('Arial', 18)
display_font = ('Arial', 32)

#Define functions

#Define Layout
#Define Frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both', expand=True)

#Define display frame layout
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify="left")
display.pack(padx=3,pady=4)

#Run main loop
root.mainloop()