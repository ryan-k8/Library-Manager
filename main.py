import logging 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk
from database import Database

db = Database('school.db')
logging.basicConfig(level=logging.DEBUG,filename='logs.log',format='%(asctime)s : %(levelname)s : %(message)s ')

def gettool_list():
    try:
        listb.delete(0,END)   #deletes entire data to resolve duplication error due to multi fn call
        for row in db.fetch():
            listb.insert(END,row) # responsible for getting data into the listbox widget
    except:
        logging.error('gettool_list() function')


def add_entries():
    try:

        if title_txt.get() == '' or author_txt.get() == '' or  borrower_txt.get()== '' or doi_txt.get() == '' or price_txt.get() == '':

           messagebox.showerror('Error','Please Fill out all fields')
           return
        db.insert(title_txt.get(),author_txt.get(),borrower_txt.get(),doi_txt.get(),price_txt.get(),dor_txt.get())
        listb.delete(0,END)
        listb.insert(END,(title_txt.get(),author_txt.get(),borrower_txt.get(),doi_txt.get(),price_txt.get(),dor_txt.get()))

        clear_fields()
        gettool_list()
    except:
        logging.error('add_entries() function')

def  selection(event):
    try:
        global cur_selection
        index = listb.curselection()[0]
        cur_selection = listb.get(index)
        print(cur_selection)
    except:
        logging.error('selection() probably tuple index error')

    title_entry.delete(0,END)
    title_entry.insert(END,cur_selection[1])

    author_entry.delete(0,END)
    author_entry.insert(END,cur_selection[2])
    
    borrower_entry.delete(0,END)
    borrower_entry.insert(END,cur_selection[3])

    doi_entry.delete(0,END)
    doi_entry.insert(END,cur_selection[4])

    price_entry.delete(0,END)
    price_entry.insert(END,cur_selection[5])

    dor_entry.delete(0,END)
    dor_entry.insert(END,cur_selection[6])


def remove_entries():
    try:  
        db.remove(cur_selection[0])
        clear_fields()
        gettool_list()
    except:
        logging.error('remove_entries')

def update_entries():
    try:
        db.update(cur_selection[0],title_txt.get(),author_txt.get(),borrower_txt.get(),doi_txt.get(),price_txt.get(),dor_txt.get())
        gettool_list()
    except:
        logging.error('remove_entries')

def clear_fields():
    try:
        title_entry.delete(0,END)
        author_entry.delete(0,END)
        borrower_entry.delete(0,END)
        doi_entry.delete(0,END)
        price_entry.delete(0,END)
        dor_entry.delete(0,END)
    except:
        logging.error('')
root = tk.ThemedTk()
root.get_themes()
root.set_theme("yaru")

# Title 
title_txt = StringVar()
title_label = Label(root,text ="Book Name", font= ('bold',10),pady=20,padx=15)
title_label.grid(row=0,column=0,sticky=W)
title_entry = ttk.Entry(root,textvariable=title_txt)
title_entry.grid(row=0,column=1)

# Author
author_txt = StringVar()
author_label = Label(root,text ="Author", font= ('bold',10),padx=15)
author_label.grid(row=0,column=2,sticky=W)
author_entry = ttk.Entry(root,textvariable=author_txt)
author_entry.grid(row=0,column=3)

# Borrower
borrower_txt = StringVar()
borrower_label = Label(root,text ="Borrower", font= ('bold',10),padx=15)
borrower_label.grid(row=0,column=4,sticky=W)
borrower_entry = ttk.Entry(root,textvariable=borrower_txt)
borrower_entry.grid(row=0,column=5)

# Date of Issue
doi_txt = StringVar()
doi_label = Label(root,text ="Issue Date", font= ('bold',10),padx=15)
doi_label.grid(row=1,column=0,sticky=W)
doi_entry = ttk.Entry(root,textvariable=doi_txt)
doi_entry.grid(row=1,column=1)

# price 
price_txt = StringVar()
price_label = Label(root,text ="Price", font= ('bold',10),padx=15)
price_label.grid(row=1,column=2,sticky=W)
price_entry = ttk.Entry(root,textvariable=price_txt)
price_entry.grid(row=1,column=3)

# Date of Return
dor_txt = StringVar()
dor_label = Label(root,text ="Return Date", font= ('bold',10),padx=15)
dor_label.grid(row=1,column=4,sticky=W)
dor_entry = ttk.Entry(root,textvariable=dor_txt)
dor_entry.grid(row=1,column=5)

# listbox
listb = Listbox(root,height=12,width=40,border=0)
listb.grid(row=3,column=0,columnspan=3,rowspan=3,pady=15,padx=20,sticky=W)

#scrollbar
scrollbar = ttk.Scrollbar(root)
scrollbar.grid(row=3,column=2)
# attaching scrollbar to listbox

listb.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command=listb.yview)

#bind selection
listb.bind('<<ListboxSelect>>',selection)


#buttons

add_btn = ttk.Button(root, text='Add ', width=12,command=add_entries)
add_btn.grid(row=2, column=0, pady=20,padx=5)

remove_btn = ttk.Button(root, text='Remove', width=12,command=remove_entries)
remove_btn.grid(row=2, column=1)

update_btn = ttk.Button(root, text='Update', width=12,command=update_entries)
update_btn.grid(row=2, column=2)

clear_btn = ttk.Button(root, text='Clear', width=12,command=clear_fields)
clear_btn.grid(row=2, column=3)

# filling listbox w/ data from database
gettool_list()

root.geometry("710x375")
root.title("Library Manager")
root.resizable(0,0)
root.iconbitmap(r'libmanager.ico') 
logging.info('Logged into the program')

root.mainloop()