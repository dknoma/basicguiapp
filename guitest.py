from tkinter import *
# Import all tkinter classes

# Create new window
# End with mainloop() to keep window persistent
root = Tk()

# title = Label(root, text="GUI Tests", bg="grey", fg="white")
title = Label(root, text="GUI Tests", bg="grey")
inputLabel = Label(root, text="Text Input", bg="grey")
inputEntry = Text(root)
formatButton = Button(root, text="Format text", fg="grey")

# sticky=n, e, s, or w for align inside the grid
title.grid(row=0, column=1)
inputLabel.grid(row=1, column=0)
inputEntry.grid(row=1, column=1, sticky=N+S+E+W)
formatButton.grid(row=2, column=1, sticky=N)

root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)

# Allows window to persist
root.mainloop()

# Text in kinter are made with Label
# Format: Label(<window>, text="Text")
# labelOne = Label(mainWindow, text="HELLO THIS IS A SIMPLE PYTHON GUI TEST")
# Pack puts label in first available space
# labelOne.pack()

# Pack layout
# topFrame = Frame(mainWindow)
# topFrame.pack()
# bottomFrame = Frame(mainWindow)
# # Packs the frame container on the bottom of the window
# bottomFrame.pack(side=BOTTOM)
#
# # Settings
# title = Label(topFrame, text="GUI Test", bg="grey", fg="black")
# # Button(whichFrame, text="button text", fg="color")
# button1 = Button(topFrame, text="Button 1", fg="blue")
# button2 = Button(topFrame, text="Button 2", fg="green")
# button3 = Button(bottomFrame, text="Button 3", fg="red")
# button4 = Button(bottomFrame, text="Button 4", fg="purple")
#
# # Pack settings
# title.pack(fill=X)
# button1.pack(side=LEFT)
# button2.pack(side=RIGHT)
# button3.pack(side=LEFT)
# button4.pack(side=RIGHT)
