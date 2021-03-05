from tkinter import * 
from tkinter import messagebox 
import pickle

def okno2(): 
tk.destroy() 
ak = Tk() 
ak.title("Регистрация") 
ak.geometry("400x600") 

def clear(): 
name_entry.delete(0, END) 
sname_entry.delete(0, END) 

ak.configure(background= backgroundColor) 

text=Label(text="Регистрация", font=("Arial", 16), background="#D7E6EB", foreground="#1D3241") 
text.place(x=200, y=145, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

name_entry = Entry(ak, bd=0, font="Arial 12", foreground="#808080") 
name_entry.place(x=200, y=200, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

sname_entry = Entry(ak, bd=0, font="Arial 12", foreground="#808080") 
sname_entry.place(x=200, y=255, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

login_entry = Entry(ak, bd=0, font="Arial 12", foreground="#808080") 
login_entry.place(x=200, y=310, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

pass_entry = Entry(ak, bd=0, font=("Arial", 12), foreground="#808080") 
pass_entry.place(x=200, y=365, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

repert_pass_entry = Entry(ak, bd=0, font=("Arial", 12), foreground="#808080") 
repert_pass_entry.place(x=200, y=420, height=30, width=250, anchor="c", bordermode=OUTSIDE) 



name_entry.insert(0, "Имя") 
sname_entry.insert(0, "Фамилия") 
login_entry.insert(0, "Логин") 
pass_entry.insert(0, "Пароль") 
repert_pass_entry.insert(0, "Повторите пароль")
tk = Tk() 
tk.title("Вход") 
tk.geometry("400x600") 
tk.configure(background= backgroundColor) 

text=Label(text="Вход", font=("Arial", 16), background="#D7E6EB", foreground="#1D3241") 
text.place(x=200, y=145, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

login_entry = Entry(tk, bd=0, font="Arial 12", foreground="#808080") 
login_entry.place(x=200, y=200, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

pass_entry = Entry(tk, bd=0, font=("Arial", 12), foreground="#808080") 
pass_entry.place(x=200, y=255, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

btn = Button(tk, text="Вход", background="#318BC9", foreground="#fff", font=("Arial", 12, "bold"), border=0, command=lambda: proverka()) 
btn.place(x=200, y=325, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

btn2 = Button(tk, text="Регистрация", background="#318BC9", foreground="#fff", font=("Arial", 12, "bold"), border=0, command=okno2) 
btn2.place(x=200, y=380, height=30, width=250, anchor="c", bordermode=OUTSIDE) 

login_entry.insert(0, "Логин") 
pass_entry.insert(0, "Пароль")
