import re
import tkinter as tk
import tkinter.scrolledtext as tkst

N = tk.N
S = tk.S
E = tk.E
W = tk.W


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
    # print(out)
    root.clipboard_clear()
    root.clipboard_append(out)
    # Print formatted output text to a second text box
    scrollText2.insert(tk.INSERT, out)


# Create new window
# End with mainloop() to keep window persistent
root = tk.Tk()
textToCopy = ''

# title = Label(root, text="GUI Tests", bg="grey", fg="white")
title = tk.Label(root, text="Text Input")
frame1 = tk.Frame(master=root, bg='grey')
scrollText1 = tkst.ScrolledText(master=frame1, wrap=tk.WORD)
formatButton = tk.Button(root, text="Format text", fg="grey")
# Bind a function to the button that activates on left click(<Button-1>)
formatButton.bind("<Button-1>", lambda inputText: formatText(scrollText1.get("1.0", tk.END)))

frame2 = tk.Frame(master=root, bg='grey')
scrollText2 = tkst.ScrolledText(master=frame2, wrap=tk.WORD)

# sticky=n, e, s, or w for align inside the grid
title.grid(row=0, column=1)
frame1.grid(row=1, column=1, sticky=N+S+E+W)
scrollText1.grid(row=1, column=1, sticky=N+S+E+W)
formatButton.grid(row=2, column=1, sticky=N)
frame2.grid(row=3, column=1, sticky=N+S+E+W)
scrollText2.grid(row=3, column=1, sticky=N+S+E+W)

root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(1, weight=1)

# Allows window to persist
root.mainloop()
