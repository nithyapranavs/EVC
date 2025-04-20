import tkinter
import tkinter.messagebox as mb
from os.path import exists
mode = 'path'
def change_link():
    global mode
    mode = 'link'
def change_path():
    global mode
    mode = 'path'
def main():
    keywrd =a.get()
    pat = b.get()
    if mode == 'path':
        f = open('1 paths.txt','a')
        if exists(pat):
            f.write(keywrd + ',' + pat+'\n')
        else:
            mb.showinfo('error','the path does not exist')
    elif mode == 'link':
        f = open('1 links.txt','a')
        f.write(keywrd+','+pat+'\n')
    f.close()
root = tkinter.Tk()
root.geometry('300x100')
frm2 = tkinter.Frame(root)
frm2.pack(side=tkinter.TOP,fill = tkinter.X)
tkinter.Radiobutton(frm2,text='link            ',value =1,command = change_link).grid(row=1)
tkinter.Radiobutton(frm2,text='path',value = 2,command = change_path).grid(row=1,column=2)
top = tkinter.Frame(root)
top.pack(side=tkinter.TOP,fill = tkinter.X)

tkinter.Label(top,text='key word            ').grid(row = 1 ,sticky = tkinter.W)
tkinter.Label(top,text='path or link        ').grid(row = 2,sticky = tkinter.W)

tkinter.Button(root,text='submit',command = main).pack(side = 'bottom')
a = tkinter.Entry(top)
b = tkinter.Entry(top)
a.grid(row = 1,column = 2)
b.grid(row =2 ,column = 2)
top.mainloop()