from mendeleev import element
from tkinter import *
from decimal import *

weight = Decimal(0)
store = Decimal(0)
button_pressed = []

store_sym = ""

getcontext().prec = 10

element_names = []
element_weight = []

# loads element symbols into element_names
for i in range(1, 119):
    elem = element(i)
    element_names.append(elem.symbol)

# loads element weights into element_weight
for i in range(1,119):
    elem = element(i)
    element_weight.append((elem.atomic_weight))

print (element_names)
print (element_weight)

names_weight = {key: value for key, value in zip(element_names, element_weight)}
print (names_weight)

# GUI
root = Tk()
root.title("Molar Mass Calculator")

frame = LabelFrame(root, padx=5, pady=5)
frame.grid(row=0, column=0, padx=10, pady=10)

e = Entry(frame, width=35, borderwidth=5)
e.grid(row=10, column=1, columnspan=17)

f = Entry(frame, width=35, borderwidth=5)
f.grid(row=9, column=1, columnspan=17)


def button_click(symbol):
    global store
    global weight
    global button_pressed
    global store_sym
    weight = Decimal(names_weight[symbol])
    button_pressed.append(Decimal(names_weight[symbol]))
    e.delete(0, END)
    e.insert(0, str(Decimal(weight + store)))
    store += weight

    store_sym += symbol
    f.delete(0, END)
    f.insert(0, str(store_sym))

def button_undo():
    global button_pressed
    global store_sym
    try:
        if len(button_pressed) != 1:
            global store

            weight_u = button_pressed.pop()
            store -= weight_u
            e.delete(0, END)
            e.insert (0, str(store))

            if store_sym[-1].islower() == True:
                store_sym = store_sym[:-2]
                f.delete(0, END)
                f.insert (0, str(store_sym))
            else:
                store_sym = store_sym[:-1]
                f.delete(0, END)
                f.insert(0, str(store_sym))

        else:
            pass
    except IndexError:
        print("Cannot undo further.")

def button_clear():
    global store
    global buton_pressed
    global store_sym
    button_pressed.clear()
    e.delete(0, END)
    e.insert(0, str(0))
    store = 0

    store_sym = ""
    f.delete(0, END)
    f.insert(0, store_sym)

# Labels
compound_label = Label(frame, text="Compound: ", padx =0, pady=0)
compound_label.grid(row=9, column=0, columnspan=3)

weight_label = Label(frame, text="Molar Mass: ", padx=0, pady=0)
weight_label.grid(row=10, column=0, columnspan=3)

# Defining and Showing Buttons
# Undo
button_undo = Button(frame, text="Undo", width=4, height = 1, command=button_undo, padx=0, pady=0)
button_undo.grid(row=9, column=16, columnspan=3)

# Clear
button_undo = Button(frame, text="Clear", width=4, height = 1, command=button_clear, padx=0, pady=0)
button_undo.grid(row=10, column=16, columnspan=3)


# Hydrogen
button_element_names = Button(frame, text=element_names[0], width=3, height=2, command=lambda: button_click('H'), padx=0, pady=0)
button_element_names.grid(row=0, column=0)

# Helium
button_element_names = Button(frame, text=element_names[1], width=3, height=2, command=lambda: button_click('He'), padx=0, pady=0)
button_element_names.grid(row=0, column=17, columnspan=17)

def Row_2_1():
    c = 0
    for a in range(2, 4):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=1, column=c)
        c+=1

def Row_2_2():
    c = 12
    for a in range(4, 10):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=1, column=c)
        c+=1

def Row_3_1():
    c=0
    for a in range(10,12):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=2, column=c)
        c+=1

def Row_3_2():
    c = 12
    for a in range(12, 18):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=2, column=c)
        c+=1

def Row_4():
    c = 0
    for a in range(18, 36):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=3, column=c)
        c+=1

def Row_5():
    c = 0
    for a in range(36, 54):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=4, column=c)
        c+=1

def Row_6_1():
    c = 0
    for a in range(54, 56):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a).symbol), padx=0, pady=0)
        button_element_names.grid(row=5, column=c)
        c += 1

def Row_6_2():
    c = 3
    for a in range(56, 71):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=7, column=c)
        c += 1

def Row_6_3():
    c = 3
    for a in range(71, 86):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=5, column=c)
        c += 1
def Row_7_1():
    c = 0
    for a in range(86, 88):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=6, column=c)
        c += 1
def Row_7_2():
    c = 3
    for a in range(88, 103):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=8, column=c)
        c += 1

def Row_7_3():
    c = 3
    for a in range(103, 118):
        button_element_names = Button(frame, text=element_names[a], width=3, height=2, command=lambda a=a: button_click(element(a+1).symbol), padx=0, pady=0)
        button_element_names.grid(row=6, column=c)
        c += 1

Row_2_1()
Row_2_2()
Row_3_1()
Row_3_2()
Row_4()
Row_5()
Row_6_1()
Row_6_2()
Row_6_3()
Row_7_1()
Row_7_2()
Row_7_3()

root.mainloop()
