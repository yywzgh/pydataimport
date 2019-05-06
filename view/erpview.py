import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("文件导入")
root.geometry('500x300')

ent = tk.Entry(root, state='readonly', width=30)
ent.grid(row=0,column=0,padx=50,pady=10)


def select_file():
    file_path = filedialog.askopenfilename()
    ent.configure(state='normal')
    ent.delete(0, tk.END)
    ent.insert(0, file_path)
    ent.configure(state='disabled')


def import_file():
    do_btn['state']=tk.DISABLED

#lb = Label(root, text = '').pack()

select_btn = tk.Button(root,text="选择文件",width=15,command=select_file).grid(row=0,column=1)

do_btn = tk.Button(root,text="确定",width=15,command=import_file)
do_btn.grid(row=1,column=0)
cancel_btn = tk.Button(root,text="取消",width=15,command=select_file).grid(row=1,column=1)

def start_gui():
    root.mainloop()

