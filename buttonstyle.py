from ttkstylist import Stylist
import tkinter as tk
from tkinter import ttk
from uuid import uuid4


options = Stylist.get_options('TButton', 'default')
print('Button options', options)

# ['shiftrelief', 'underline', 'text', 'space', 'background', 
# 'image', 'borderwidth', 'embossed', 'relief', 'focusthickness', 
# 'width', 'justify', 'focuscolor', 'compound', 'anchor', 'padding', 
# 'font', 'foreground', 'stipple', 'wraplength']

root = tk.Tk()
style = ttk.Style()
style.theme_use('default')

ttkstyle = '{}.TButton'.format(uuid4())

style.configure(
    style=ttkstyle,
    background='blue',
    foreground='white',
    padding=5,
    font=('Helvetica', 12, 'bold')
)

style.map(
    style=ttkstyle,
    background=[('disabled', 'green'), ('hover', 'red'), 
                ('pressed', 'blue'), ('focus', 'black')],
    foreground=[('disabled', 'yellow'), ('hover', 'orange'), 
                ('pressed', 'white'), ('focus', 'yellow')],
    focuscolor=[('focus', 'white'), ('!focus', 'gray')]
)

ttk.Button(style=ttkstyle, text="Styled Button").pack(padx=10, pady=10)
ttk.Button(text="Regular Button").pack(padx=10, pady=10)

root.mainloop()