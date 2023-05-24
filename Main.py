from tkinter import *
from tkinter import filedialog
from subprocess import call

if __name__ == "__main__":

############################
#   Main Window Start
############################
    win = Tk()
    win.resizable(False, False)
    win.title("Adress Book")
    win.geometry("500x600")

    def rr(s):
       pass

        
    def Add_Save(e):
        def s(c):
            call(["python", c])
        
        Label(master=win, text=e).pack()
        Button(master=win, text="Run", command=lambda: s(seee)).pack()
        win2.destroy()
        
    def get_save(master):
        global seee
        o = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python Scripts", ".py")])
        seee = Text(master=master, width=30, background="lightgray")
        seee.place(x=0, y=25)
        seee.insert('1.0', o)



    def OpenNew():
        call(["python", "CodeEditor.py"])
    
    def Run():
        OpenFile = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python script",".py")])
        call(["python", OpenFile])
    
    def Save():
        global win2
        win2 = Toplevel(win)
        win2.title("Save New Open")
        win2.geometry("500x200")
        Label(master=win2, text="Name: ").grid(column=0, row=0)
        Name = Text(master=win2, width=20, height=1, padx=2)
        Name.grid(column=1, row=0)
        Button(master=win2, text="Open", command=lambda: get_save(win2)).grid(column=2, row=0)
        Button(master=win2, text="Save", command=lambda: Add_Save(Name.get('1.0',END))).grid(column=3, row=0)
        win2.mainloop()



    MainMenuBar = Menu(win)
    
    FileMenu = Menu(MainMenuBar, tearoff=0)
    MainMenuBar.add_cascade(label="File", menu=FileMenu)
    FileMenu.add_command(label="New", command=OpenNew)
    FileMenu.add_command(label="Run", command=Run)
    FileMenu.add_command(label="Save", command=Save)


    win.config(menu=MainMenuBar)
    win.mainloop()