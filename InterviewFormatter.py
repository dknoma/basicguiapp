# -*- coding: utf-8 -*-
import re
import tkinter as tk


class HTMLFormatter:
    def __init__(self):
        self.url = ''

    def tsformat(self, mathobject):
        return ''

    def urlformat(self, matchobject):
        self.url = '[url=' + matchobject.group(0) + ']INSERT TEXT HERE[/url]'
        return str(self.url)


class GUIApp:
    def __init__(self):
        # Create new window
        # End with mainloop() to keep window persistent
        self.root = tk.Tk()
        self.root.title('Discord Interview Formatter')

        # Need boxes for username formatters
        # [color=#660066][/color]
        self.interviewerName = ''
        self.intervieweeName = ''
        self.irSMWCName = ''
        self.ieSMWCName = ''
        self.interviewerColor = ''
        self.intervieweeColor = ''

        # title = Label(root, text="GUI Tests", bg="grey", fg="white")
        interviewer = tk.Label(self.root, text="Interviewer:")
        interviewee = tk.Label(self.root, text="Interviewee:")
        self.interviewerNameInput = tk.Entry(self.root)
        self.intervieweeNameInput = tk.Entry(self.root)
        irSMWC = tk.Label(self.root, text="SMWC Name:")
        ieSMWC = tk.Label(self.root, text="SMWC Name:")
        self.irSMWCNameInput = tk.Entry(self.root)
        self.ieSMWCNameInput = tk.Entry(self.root)
        interviewerColor = tk.Label(self.root, text="Color in hex:")
        intervieweeColor = tk.Label(self.root, text="Color in hex:")
        self.interviewerColorInput = tk.Entry(self.root)
        self.intervieweeColorInput = tk.Entry(self.root)

        title = tk.Label(self.root, text="Text Input")
        self.text1 = tk.Text(self.root)
        self.text2 = tk.Text(self.root)
        formatButton = tk.Button(self.root, text="Format text", fg="purple")
        # Bind a function to the button that activates on left click(<Button-1>)
        formatButton.bind("<Button-1>", lambda inputText: self.formatText(self.text1.get("1.0", tk.END)))

        interviewer.grid(row=0, column=0)
        self.interviewerNameInput.grid(row=0, column=1, sticky="W")
        interviewee.grid(row=1, column=0)
        self.intervieweeNameInput.grid(row=1, column=1, sticky="W")

        irSMWC.grid(row=0, column=2)
        self.irSMWCNameInput.grid(row=0, column=3)
        ieSMWC.grid(row=1, column=2)
        self.ieSMWCNameInput.grid(row=1, column=3)

        interviewerColor.grid(row=0, column=4, sticky="W")
        self.interviewerColorInput.grid(row=0, column=5, sticky="W")
        intervieweeColor.grid(row=1, column=4, sticky="W")
        self.intervieweeColorInput.grid(row=1, column=5, sticky="W")

        # sticky=n, e, s, or w for align inside the grid
        title.grid(row=2, column=1)
        self.text1.grid(row=3, column=0, columnspan=6, sticky="NSEW")
        formatButton.grid(row=4, column=1, sticky="NE")
        self.text2.grid(row=5, column=0, columnspan=6, sticky="NSEW")

        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(5, weight=1)

        # Allows window to persist
        self.root.mainloop()

    def getNameInfo(self):
        try:
            self.interviewerName = re.escape(self.interviewerNameInput.get())
            self.intervieweeName = re.escape(self.intervieweeNameInput.get())
            self.irSMWCName = re.escape(self.irSMWCNameInput.get())
            self.ieSMWCName = re.escape(self.ieSMWCNameInput.get())
            self.interviewerColor = self.interviewerColorInput.get()
            self.intervieweeColor = self.intervieweeColorInput.get()
            if self.interviewerName == '' or self.intervieweeName == '' or self.irSMWCName == '' or self.ieSMWCName == '' or self.interviewerColor == '' or self.intervieweeColor == '':
                err = 'One or more fields are empty.'
                self.text2.delete('1.0', tk.END)
                self.text2.insert(tk.INSERT, err)
                raise Exception(err)
            print("Interviewer: " + self.interviewerName)
            print("Color: " + self.interviewerColor)
            print("Interviewee: " + self.intervieweeName)
            print("Color: " + self.intervieweeColor)
        except Exception as e:
            print('Exception: ' + str(e))
            raise Exception(str(e))

    def formatText(self, inputText):
        try:
            self.getNameInfo()
            print("formatting...")
            # HTTP regex
            urlRegex = r'(?P<url>https?://[^\s]+)'
            # Discord timestamp regex
            tsRegex = r'(\[\d+:\d+\s(AM|PM)\]\s)'
            # HTML Discord Interview Formatter
            formatter = HTMLFormatter()
            urlPattern = re.compile(urlRegex)
            timestampPattern = re.compile(tsRegex)
            # Remove all timestamps
            text = timestampPattern.sub(formatter.tsformat, inputText)
            # Format all URLs to be SMWC post ready
            out = urlPattern.sub(formatter.urlformat, text)
            # print(out)
            out = re.sub(self.interviewerName, self.irSMWCName, out)
            out = re.sub(self.intervieweeName, self.ieSMWCName, out)

            # Copy formatted output to the clipboard
            self.root.clipboard_clear()
            self.root.clipboard_append(out)
            # Clear the output box and print the formatted output text to the box
            self.text2.delete('1.0', tk.END)
            self.text2.insert(tk.INSERT, out)
        except Exception as e:
            print('Exception: ' + str(e))


if __name__ == '__main__':
    root = GUIApp()

