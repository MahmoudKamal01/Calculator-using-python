from tkinter import *
from math import pi, e, sin, cos, tan, log, asin, acos, atan, factorial, degrees, radians
win = Tk()  # This is to create a basic window
win.geometry("484x554")  # this is for the size of the window
win.title("Calculator")

# 'clickButton' function :
# This Function continuously updates the input field whenever you enter a number
# 'StringVar()' :It is used to get the instance of input field

input_text = StringVar()
ans= ""
expression= ""

def clickButton(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# 'bt_clear' function :This is used to clear
# the input field

def clearAll():
    global expression
    expression = ""
    input_text.set("")

def clearButton():
    global expression
    input_text.set(input_text.get()[0:-1])
    expression = input_text.get()

def equal_button():
    global expression, ans
    try:
        result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
        input_text.set(result)
        ans = input_text.get()
        expression= ""
    except:
        input_text.set(" syntax error ")
        expression = ""

#frame for the input field

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="grey", highlightcolor="black",
                    highlightthickness=2)

input_frame.pack(side=TOP)

#input field inside the 'Frame'

input_field = Entry(input_frame, font=('arial', 20, 'bold'), textvariable=input_text, width=32, bg="#eee", bd=0,
                    justify=LEFT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field

# Let us creating another 'Frame' for the button below the 'input_frame'

btns_frame = Frame(win, width=500, height=600, bg="lightblue")
btns_frame.pack()

button_label_list = []
w, h, b = 15, 3, 4
def adv_btn():

    global button_label_list
    win.geometry("484x675")
    button_label_list.append([Button(btns_frame, text="arcsin", command=lambda:clickButton("asin("), fg="black", bd=b, bg="#686e5e", cursor="hand2",width=w,height=h),
                              Button(btns_frame, text="arccos", command=lambda:clickButton("acos("), fg="black", bd=b, bg="#686e5e", cursor="hand2",width=w,height=h),
                              Button(btns_frame, text="arctan", command=lambda:clickButton("atan("), fg="black", bd=b, bg="#686e5e", cursor="hand2",width=w,height=h),
                              Button(btns_frame, text="modulus", command=lambda:clickButton("%"), fg="black", bd=b, bg="#686e5e", cursor="hand2",width=w,height=h),
                              Button(btns_frame, text="Deg", command=lambda: clickButton("degrees("), fg="black", bd=b, bg="#686e5e", cursor="hand2",width=w,height=h),
                              Button(btns_frame, text="Rad", command=lambda: clickButton("radians("), fg="black", bd=b, bg="#686e5e", cursor="hand2",width=w,height=h),
                              Button(btns_frame, text="log", command=lambda: clickButton("log("), fg="black", bd=b, bg="#686e5e", cursor="hand2",width=w,height=h),
                              Button(btns_frame, text="round", command=lambda: clickButton("round("), fg="black", bd=b, bg="#686e5e", cursor="hand2",width=w,height=h),
                              Button(btns_frame, text="↑", command=lambda:up(), fg="black", bd=b, bg="#f59e42", cursor="hand2",width=w,height=h)])

    button_label_list[0][0].grid(row=8,column=0, padx=1, pady=1)
    button_label_list[0][1].grid(row=8, column=1, padx=1, pady=1)
    button_label_list[0][2].grid(row=8, column=2, padx=1, pady=1)
    button_label_list[0][3].grid(row=8, column=3, padx=1, pady=1)
    button_label_list[0][4].grid(row=9,column=0, padx=1, pady=1)
    button_label_list[0][5].grid(row=9, column=1, padx=1, pady=1)
    button_label_list[0][6].grid(row=9, column=2, padx=1, pady=1)
    button_label_list[0][7].grid(row=9, column=3, padx=1, pady=1)
    button_label_list[0][8].grid(row=5, column=3, padx=1, pady=1)
    button_label_list.clear()


def up():
    win.geometry("484x554")
    button_label_list.append([Button(btns_frame, text="Advanced", fg="black", bd=b, bg="#38f9fc", cursor="hand2", width=15, height=3,
                      command=lambda: adv_btn())])
    button_label_list[0][0].grid(row=5, column=3, padx=1, pady=1)
    button_label_list.clear()


# first row

allclear = Button(btns_frame, text="AC",fg="black", width=31, height=h, bd=b, bg="#f59e42", cursor="hand2",
               command=lambda: clearAll()).grid(row=0, column=0, columnspan=2, padx=1, pady=1)

clear = Button(btns_frame, text="C", fg="black", width=w, height=h, bd=b, bg="red", cursor="hand2",
               command=lambda: clearButton()).grid(row=0, column=2, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
                command=lambda: clickButton("/")).grid(row=0, column=3, padx=1, pady=1)

# second row

seven = Button(btns_frame, text="7", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
               command=lambda: clickButton(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
               command=lambda: clickButton(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
              command=lambda: clickButton(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
                  command=lambda: clickButton("*")).grid(row=1, column=3, padx=1, pady=1)

# third row

four = Button(btns_frame, text="4", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
              command=lambda: clickButton(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
              command=lambda: clickButton(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
             command=lambda: clickButton(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row

one = Button(btns_frame, text="1", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
             command=lambda: clickButton(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
             command=lambda: clickButton(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
               command=lambda: clickButton(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
              command=lambda: clickButton("+")).grid(row=3, column=3, padx=1, pady=1)

# fifth row

zero = Button(btns_frame, text="0", fg="black", width=31, height=h, bd=b, bg="#fff", cursor="hand2",
              command=lambda: clickButton(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

answer = Button(btns_frame, text="ans", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton(ans)).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=w, height=h, bd=b, bg="#38f9fc", cursor="hand2",
                command=lambda: equal_button()).grid(row=4, column=3, padx=1, pady=1)

# sixth row

point = Button(btns_frame, text=".", fg="black", width=w, height=h, bd=b, bg="#fff", cursor="hand2",
               command=lambda: clickButton(".")).grid(row=5, column=0, padx=1, pady=1)

bracket1 = Button(btns_frame, text="(", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton("(")).grid(row=5, column=1, padx=1, pady=1)

bracket2 = Button(btns_frame, text=")", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton(")")).grid(row=5, column=2, padx=1, pady=1)

advanced = Button(btns_frame, text="Advanced", fg="black", bg="#38f9fc", cursor="hand2", width=w, height=h, bd=b,
                 command=lambda:adv_btn()).grid(row=5, column=3, padx=1, pady=1)
# seventh row

sin_btn = Button(btns_frame, text="sin", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton("sin(")).grid(row=6, column=0, padx=1, pady=1)

cos_btn = Button(btns_frame, text="cos", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton("cos(")).grid(row=6, column=1, padx=1, pady=1)

tan_btn = Button(btns_frame, text="tan", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton("tan(")).grid(row=6, column=2, padx=1, pady=1)

pie=3.1415
pi = Button(btns_frame, text="π", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton(pie)).grid(row=6, column=3, padx=1, pady=1)

# eighth row

fact = Button(btns_frame, text="!", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton("factorial(")).grid(row=7, column=0, padx=1, pady=1)

eie = 2.7182
e = Button(btns_frame, text="𝓮", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton(eie)).grid(row=7, column=1, padx=1, pady=1)

power = Button(btns_frame, text="^", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton("**")).grid(row=7, column=2, padx=1, pady=1)

root = Button(btns_frame, text="√", fg="black", width=w, height=h, bd=b, bg="#686e5e", cursor="hand2",
               command=lambda: clickButton("**1/")).grid(row=7, column=3, padx=1, pady=1)

win.iconbitmap("icon.ico")
win.mainloop()

