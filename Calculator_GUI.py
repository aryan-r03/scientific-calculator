import customtkinter as ctk
import math

ctk.set_appearance_mode("dynamic")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Calculator")
app.geometry("420x500")
app.resizable(width=True, height=True)

expression = ""

def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

equation = ctk.StringVar()
entry = ctk.CTkEntry(app, textvariable=equation, width=400, height=50,
                     font=("Helvetica", 28), justify="center")
entry.grid(row=0, column=0, columnspan=8, padx=10, pady=10)

def make_btn(txt, r, c, cmd=None, color=None):
    return ctk.CTkButton(app, text=txt, width=80, height=70,
                         corner_radius=15,
                         fg_color=color if color else "#333",
                         hover_color="#555",
                         font=("Helvetica", 18),
                         command=cmd).grid(row=r, column=c, padx=5, pady=5)

buttons = [
    ("(",1,2, lambda: press("(")), (")",1,3, lambda: press(")")),
    ("7",2,2, lambda: press("7")), ("8",2,3, lambda: press("8")),
    ("9",2,4, lambda: press("9")), ("×",2,5, lambda: press("*")),
    ("4",4,2, lambda: press("4")), ("5",4,3, lambda: press("5")),
    ("6",4,4, lambda: press("6")), ("-",4,5, lambda: press("-")),
    ("1",5,2, lambda: press("1")), ("2",5,3, lambda: press("2")),
    ("3",5,4, lambda: press("3")), ("+",5,5, lambda: press("+")),
    ("0",6,2, lambda: press("0")),
    ("00",6,3, lambda: press("00")),
    (".",6,4, lambda: press(".")),
    ("C",1,4, clear),
    ("⌫",1,5, backspace),
    ("=",6,5, calculate),
]

for txt, r, c, cmd in buttons:
    make_btn(txt, r, c, cmd,
             color="#ff9f0a" if txt in {"+","-","×","/","="} else "#444")

app.mainloop()