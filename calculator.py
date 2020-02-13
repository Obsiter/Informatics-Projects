from tkinter import *

root = Tk()
root.title('Kalkulator')


#Definiramo spremnik za brojeve
e = Entry(root, width=55, borderwidth=3)
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


#definiramo funkcije za gumbove
def button_click(number):
    broj = e.get()
    e.delete(0, END)
    e.insert(0, str(broj) + str(number))

#Tipka za ocistiti ekran(C)
def button_clear():
    e.delete(0, END)

#Tipka za zbrajanje
def plus():
    global prvi
    global znak
    znak = "+"
    prvi = int(e.get())
    e.delete(0, END)

#Tipka za oduzimanje
def minus():
    global prvi
    global znak
    znak = "-"
    prvi = int(e.get())
    e.delete(0, END)

#Tipka jednako
def equal():
    drugi = int(e.get())
    e.delete(0, END)
    if znak != "+":
        e.insert(0, prvi - drugi)
    else:
        e.insert(0, prvi + drugi)

#Tipka za ugasiti kalkulator
def destroy():
    root.destroy()


#Svakome gumbu se daje ime, vrijednost, te funkcija koju odrađuje
button_1 = Button(root, text='1', padx=55, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=55, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=55, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=55, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=55, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=55, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=55, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=55, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=55, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=55, pady=20, command=lambda: button_click(0))
button_plus = Button(root, text='+', padx=55, pady=20, command=plus)
button_minus = Button(root, text='-', padx=55, pady=20, command=minus)
button_equal = Button(root, text='=', padx=55, pady=20, command=equal)
button_clear = Button(root, text='C', padx=55, pady=20, command=button_clear)
button_quit = Button(root, text='Izlaz', padx=47, pady=20, command=destroy)


#Svaki gumb se postavlja u stupac i red, tako zvani Grid
button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=1, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)
button_9.grid(row=3, column=3)

button_0.grid(row=4, column=1)
button_plus.grid(row=4, column=2)
button_minus.grid(row=4, column=3)

button_clear.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_quit.grid(row=5, column=3)


#Pokrecemo program funkciom mainloop()
root.mainloop()
