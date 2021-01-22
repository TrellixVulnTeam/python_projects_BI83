from tkinter import *

root = Tk()
root.title("Simple Calculator")

inputBox = Entry(root, width=35, borderwidth=5)
inputBox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
numbers = []


def button_click(value):
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + str(value))


def button_clear():
    inputBox.delete(0, END)


def button_add():
    first_num = inputBox.get()
    global f_num
    f_num = []
    f_num.append(int(first_num))
    inputBox.delete(0, END)

def button_equal():
    second_num = inputBox.get()
    global total, s_num
    total = 0
    s_num = int(second_num)
    inputBox.delete(0, END)
    for num in f_num:
        total = total+num

    inputBox.insert(0, total+s_num)


# Buttons on Calculator
num1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
num2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
num3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
num4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
num5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
num6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
num7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
num8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
num9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
num0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0))

# Additional Buttons
button_add = Button(root, text="+", padx=20, pady=10, command=button_add)
button_equal = Button(root, text="=", padx=60, pady=10, command=button_equal)
button_clear = Button(root, text="Clear", padx=50, pady=10, command=button_clear)

# Display Buttons

num1.grid(row=1, column=0)
num2.grid(row=1, column=1)
num3.grid(row=1, column=2)

num4.grid(row=2, column=0)
num5.grid(row=2, column=1)
num6.grid(row=2, column=2)

num7.grid(row=3, column=0)
num8.grid(row=3, column=1)
num9.grid(row=3, column=2)

num0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
