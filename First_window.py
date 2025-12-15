from tkinter import *
import Game_window

window_width = 700
window_height = 500
font_type = ('Times New Roman', 12)
ffont_type = ('Times New Roman', 14, 'bold')
bg_color='#eae2b7'
bg_btn = '#eae299'

def Show_game(mode):
    window1.destroy()
    if mode == 1:
        Game_window.human_vs_human()
    elif mode == 2:
        Game_window.human_play()
    elif mode == 3:
        Game_window.computer_play()

def resize_and_center(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def show_names_frame():
    first_frame.place_forget()
    names_frame.place(relx=0.5, rely=0.5, anchor='center')

def show_first_frame(event):
    names_frame.place_forget()
    first_frame.place(relx=0.5, rely=0.5, anchor='center')


window1 = Tk()
window1.title('Connect4 Game')
window1.configure(bg=bg_color)
resize_and_center(window1, window_width, window_height)

first_frame = Frame(window1, bg=bg_color)
first_frame.place(relx=0.5, rely=0.5, anchor='center')

Label(first_frame, text='Did You Miss Us? Cause We Missed You', font=ffont_type, bg=bg_color).grid(row=0, column=0, columnspan=2, pady=5)
Label(first_frame, text='What Is Your Choice For Today', font=ffont_type, bg=bg_color).grid(row=1, column=0, columnspan=2, pady=5)

Button(first_frame, text='You VS Your Friend', font=font_type, width=15, height=1, cursor="hand2", command=show_names_frame, bg=bg_btn).grid(row=2, column=0, columnspan=2, pady=5)
Button(first_frame, text='You VS Me', font=font_type, width=15, height=1, cursor="hand2", command=lambda: Show_game(2), bg=bg_btn).grid(row=3, column=0, columnspan=2, pady=5)
Label(first_frame, text='Want To Watch Only?', font=ffont_type, bg=bg_color).grid(row=4, column=0, columnspan=2, pady=5)
Button(first_frame, text='Computers War', font=font_type, width=15, height=1, cursor="hand2", command=lambda: Show_game(3), bg=bg_btn).grid(row=5, column=0, columnspan=2, pady=5)

names_frame = Frame(window1, bg=bg_color)

Label(names_frame, text="Enter Players names", font=ffont_type, bg=bg_color).grid(row=0, column=0, columnspan=2, pady=5)

Label(names_frame, text="Player 1's Name", font=ffont_type, bg=bg_color).grid(row=1, column=0, pady=5)
name1 = Entry(names_frame, font=font_type).grid(row=2, column=0, pady=5, padx=5)

Label(names_frame, text="Player 2's Name", font=ffont_type, bg=bg_color).grid(row=1, column=1, pady=5)
name2 = Entry(names_frame, font=font_type).grid(row=2, column=1, pady=5, padx=5)

Button(names_frame, text='START', font=font_type, width=10, height=1, cursor="hand2", command=lambda: Show_game(1), bg=bg_btn).grid(row=3, column=0, columnspan=2, pady=10)

back_label = Label(names_frame, text='Back', font=('Times New Roman',10, 'underline'), cursor='hand2', bg=bg_color)
back_label.grid(row=4, column=0, columnspan=2, pady=5)
back_label.bind("<Button-1>", show_first_frame)

window1.mainloop()
