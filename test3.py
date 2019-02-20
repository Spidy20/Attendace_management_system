from tkinter import *

root = Tk()

def testVal(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True

entry = Entry(root, validate="key")
entry['validatecommand'] = (entry.register(testVal),'%P','%d')
entry.pack()

root.mainloop()