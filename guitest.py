from tkinter import *
# Import all tkinter classes


class HTMLFormatter:
    def __init__(self):
        self.url = ''

    def tsformat(self, mathobject):
        return ''

    def urlformat(self, matchobject):
        self.url = '[url=' + matchobject.group(0) + ']INSERT TEXT HERE[/url]'
        return str(self.url)


def formatText(inputText):
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
    inputText = timestampPattern.sub(formatter.tsformat, inputText)
    # Format all URLs to be SMWC post ready
    out = urlPattern.sub(formatter.urlformat, inputText)
    print(out)
    root.clipboard_clear()
    root.clipboard_append(out)


# Create new window
# End with mainloop() to keep window persistent
root = Tk()
textToCopy = ''

# title = Label(root, text="GUI Tests", bg="grey", fg="white")
title = Label(root, text="Text Input")
inputEntry = Text(root)
formatButton = Button(root, text="Format text", fg="grey")
# Bind a function to the button that activates on left click(<Button-1>)
formatButton.bind("<Button-1>", lambda inputText: formatText(inputEntry.get("1.0", END)))

# sticky=n, e, s, or w for align inside the grid
title.grid(row=0, column=1)
inputEntry.grid(row=1, column=1, sticky=N+S+E+W)
formatButton.grid(row=2, column=1, sticky=N)

root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)

# Allows window to persist
root.mainloop()
