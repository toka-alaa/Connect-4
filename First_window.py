from tkinter import *
from Connect4_GUI import Connect4GUI

window_width = 700
window_height = 500
font_type = ('Times New Roman', 12)
ffont_type = ('Times New Roman', 14, 'bold')
bg_color='#eae2b7'
bg_btn = '#eae299'

def Show_game(mode):
    window1.destroy()
    Connect4GUI(mode)

def resize_and_center(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    root.geometry(f"{width}x{height}+{x}+{y}")


window1 = Tk()
window1.title('Connect4 Game')
window1.configure(bg=bg_color)
resize_and_center(window1, window_width, window_height)

first_frame = Frame(window1, bg=bg_color)
first_frame.place(relx=0.5, rely=0.5, anchor='center')

Label(first_frame, text='Did You Miss Us? Cause We Missed You', font=ffont_type, bg=bg_color).grid(row=0, column=0, columnspan=2, pady=5)
Label(first_frame, text='What Is Your Choice For Today', font=ffont_type, bg=bg_color).grid(row=1, column=0, columnspan=2, pady=5)

Button(first_frame, text='You VS Your Friend', font=font_type, width=15, height=1, cursor="hand2", command=lambda: Show_game("HH"), bg=bg_btn).grid(row=2, column=0, columnspan=2, pady=5)
Button(first_frame, text='You VS Me', font=font_type, width=15, height=1, cursor="hand2", command=lambda: Show_game("HC"), bg=bg_btn).grid(row=3, column=0, columnspan=2, pady=5)
Label(first_frame, text='Want To Watch Only?', font=ffont_type, bg=bg_color).grid(row=4, column=0, columnspan=2, pady=5)
Button(first_frame, text='Computers War', font=font_type, width=15, height=1, cursor="hand2", command=lambda: Show_game("CC"), bg=bg_btn).grid(row=5, column=0, columnspan=2, pady=5)

window1.mainloop()
