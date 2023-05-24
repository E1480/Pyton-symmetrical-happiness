from tkinter import *
from tkinter import filedialog
import ctypes
import re

# Increas Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Setup Tkinter
root = Tk()
root.title("Code Editor")
root.geometry('500x500')


# Execute the Programm
def execute(event=None):

    file = filedialog.asksaveasfile(defaultextension='.py',
                                    filetypes=[("Python script",".py")])
    file.write(str(editArea.get('1.0', END)))
    file.close()
    root.destroy()
    

    # Write the Content to the Temporary File
   # with open('run.py', 'w', encoding='utf-8') as f:
   #     f.write(editArea.get('1.0', END))
   
   
# Register Changes made to the Editor Content
def changes(event=None):
    global previousText

    # If actually no changes have been made stop / return the function
    if editArea.get('1.0', END) == previousText:
        return

    # Remove all tags so they can be redrawn
    for tag in editArea.tag_names():
        editArea.tag_remove(tag, "1.0", "end")

    # Add tags where the search_re function found the pattern
    i = 0
    for pattern, color in repl:
        for start, end in search_re(pattern, editArea.get('1.0', END)):
            editArea.tag_add(f'{i}', start, end)
            editArea.tag_config(f'{i}', foreground=color)

            i+=1

    previousText = editArea.get('1.0', END) 

def search_re(pattern, text, groupid=0):
    matches = []

    text = text.splitlines()
    for i, line in enumerate(text):
        for match in re.finditer(pattern, line):

            matches.append(
                (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
            )

    return matches


def rgb(rgb):
    return "#%02x%02x%02x" % rgb


previousText = ''

# Define colors for the variouse types of tokens
normal = rgb((234, 234, 234))
keywords = rgb((234, 95, 95))
comments = rgb((95, 234, 165))
string = rgb((234, 162, 95))
function = rgb((95, 211, 234))
background = rgb((42, 42, 42))
font = 'Consolas 15'


# Define a list of Regex Pattern that should be colored in a certain way
repl = [
    ['(^| )(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)($| )', keywords],
    ['".*?"', string],
    ['\'.*?\'', string],
    ['#.*?$', comments],
    ['(^| )(print)($| )', function],
]

# Make the Text Widget
# Add a hefty border width so we can achieve a little bit of padding
editArea = Text(
    root,
    background=background,
    foreground=normal,
    insertbackground=normal,
    relief=FLAT,
    borderwidth=30,
    font=font
)

# Place the Edit Area with the pack method
editArea.pack(
    fill=BOTH,
    expand=1
)

# Bind the KeyRelase to the Changes Function
editArea.bind('<KeyRelease>', changes)

# Bind Control + R to the exec function
root.bind('<Control-s>', execute)

changes()
root.mainloop()