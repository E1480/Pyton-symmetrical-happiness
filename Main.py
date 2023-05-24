from tkinter import *
from tkinter import filedialog
from subprocess import call

if __name__ == "__main__":

    def OpenNew():
        call(["python", "CodeEditor.py"])
    
    def Run():
        e = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python script",".py")])
        call(["python", e])

############################
#   Main Window Start
############################
    win = Tk()
    win.resizable(False, False)
    win.title("Adress Book")
    win.geometry("500x600")


    MainMenuBar = Menu(win)
    
    FileMenu = Menu(MainMenuBar, tearoff=0)
    MainMenuBar.add_cascade(label="File", menu=FileMenu)
    FileMenu.add_command(label="New", command=OpenNew)
    FileMenu.add_command(label="Run", command=Run)


    win.config(menu=MainMenuBar)
    win.mainloop()