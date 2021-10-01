from tkinter import *



root = Tk()
root.title('Calculator')

Ent = Entry(root, width=50, borderwidth=10, bg='black', fg='white', font='sans, 9')
Ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def add_button(number):
    current = Ent.get()
    Ent.delete(0, END)
    Ent.insert(0, str(current)+str(number))
    
    
  
def clear_button():
    Ent.delete(0, END)

    


def eq_button():
    second_number = Ent.get()
    Ent.delete(0, END)

    #condition.....
    if math == "addition":
       Ent.insert(0, int(f_num) + int(second_number))

    elif math == "subtraction":
       Ent.insert(0, int(f_num) - int(second_number))

    elif math == "multiplication":
       Ent.insert(0, int(f_num) * int(second_number))

    elif math == "division":
       Ent.insert(0, int(f_num) / int(second_number))
   


#add, sub, mul, div....................
def pls_button():
    pls_number = Ent.get()
    global f_num
    global math
    f_num = pls_number
    math = "addition"
    Ent.delete(0, END)


def sub_button():
    sub_number = Ent.get()
    global f_num
    global math
    f_num = sub_number
    math = "subtraction"
    Ent.delete(0, END)


def mul_button():
    mul_number = Ent.get()
    global f_num
    global math
    f_num = mul_number
    math = "multiplication"
    Ent.delete(0, END)


def div_button():
    div_number = Ent.get()
    global f_num
    global math
    f_num = div_number
    math = "division"
    Ent.delete(0, END)




    


button1 = Button(root, text=1, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(1))
button1.grid(row=1, column=0)

button2 = Button(root, text=2, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(2))
button2.grid(row=1, column=1)

button3 = Button(root, text=3, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(3))
button3.grid(row=1, column=2)

button4 = Button(root, text=4, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(4))
button4.grid(row=2, column=0)

button5 = Button(root, text=5, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(5))
button5.grid(row=2, column=1)

button6 = Button(root, text=6, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(6))
button6.grid(row=2, column=2)

button7 = Button(root, text=7, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(7))
button7.grid(row=3, column=0)

button8 = Button(root, text=8, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(8))
button8.grid(row=3, column=1)

button9 = Button(root, text=9, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(9))
button9.grid(row=3, column=2)

button0 = Button(root, text=0, fg='black', bg='purple', font='sans, 20', padx=30, command=lambda:add_button(0))
button0.grid(row=4, column=0)

button_clear = Button(root, text='Clear', fg='white', bg='purple', font='sans, 20', padx=5, command=clear_button)
button_clear.grid(row=4, column=1, columnspan=1)

button_eq = Button(root, text='=', fg='black', bg='yellow', font='sans, 20', padx=30, command=eq_button )
button_eq.grid(row=6, column=1, columnspan=1)


#add, sub, mul, div.............................
button_pls = Button(root, text='+', fg='black', bg='green', font='sans, 20', padx=30, command=pls_button)
button_pls.grid(row=5, column=0)

button_sub = Button(root, text='-', fg='black', bg='green', font='sans, 20', padx=33, command=sub_button)
button_sub.grid(row=5, column=1)

button_mul = Button(root, text='*', fg='black', bg='green', font='sans, 20', padx=33, command=mul_button)
button_mul.grid(row=5, column=2)

button_div = Button(root, text='/', fg='black', bg='green', font='sans, 20', padx=33, command=div_button)
button_div.grid(row=4, column=2)




root.mainloop()

