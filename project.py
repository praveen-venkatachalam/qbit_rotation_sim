import os
import qiskit
import tkinter

#Define Window
root = tkinter.Tk()
root.title('Qbit Rotation Simulator')

#set size
root.geometry('435x330')
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
button_frame = tkinter.LabelFrame(root)
display_frame.pack()
button_frame.pack(fill='both', expand=True)

#Define display frame layout
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify="left")
display.pack(padx=3,pady=4)

#First Row of buttons
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X')
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y')
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z')
x_gate.grid(row=0,column=0,ipadx=45, pady=1)
y_gate.grid(row=0,column=1,ipadx=45, pady=1)
z_gate.grid(row=0,column=2,ipadx=53, pady=1, sticky='E')

#Second Row of Buttons
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RX')
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RY')
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RZ')
Rx_gate.grid(row=1,column=0, columnspan=1, pady=1, sticky='WE')
Ry_gate.grid(row=1,column=1, columnspan=1, pady=1, sticky='WE')
Rz_gate.grid(row=1,column=2, columnspan=1, pady=1, sticky='WE')

#Third Row of buttons
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S')
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD')
hadamard = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H')
s_gate.grid(row=2,column=0, columnspan=1, pady=1, sticky='WE')
sd_gate.grid(row=2,column=1, pady=1, sticky='WE')
hadamard.grid(row=2,column=2, rowspan=2, pady=1, sticky='WENS')

#Fourth row of buttons
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T')
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD')
t_gate.grid(row=3,column=0, pady=1, sticky='WE')
td_gate.grid(row=3,column=1, pady=1, sticky='WE')

#Quit and Visualize button
quit = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Quit', command=root.destroy)
visualize = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Visualize')
quit.grid(row=4,column=0, columnspan=2,ipadx=5, pady=1, sticky='WE')
visualize.grid(row=4,column=2, columnspan=1,ipadx=8, pady=1, sticky='WE')

#Clear button
clear_button = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Clear')
clear_button.grid(row=5,column=0, columnspan=3, sticky='WE')

#About button
about_button = tkinter.Button(button_frame, font=button_font, bg=buttons, text='About')
about_button.grid(row=6,column=0, columnspan=3, sticky='WE')


#Run main loop
root.mainloop()