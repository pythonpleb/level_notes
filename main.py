from tkinter import *

root = Tk()
root.title("Level Notes")

default_rows_num = 10
count = default_rows_num + 1


def table(num):
    point = Entry(root, borderwidth=3)
    bs = Entry(root, borderwidth=3)
    hi = Entry(root, borderwidth=3)
    ifs = Entry(root, borderwidth=3)
    fs = Entry(root, borderwidth=3)
    elev = Entry(root, borderwidth=3)
    desc = Entry(root, borderwidth=3)

    point.grid(row=num, column=1)
    bs.grid(row=num, column=2)
    hi.grid(row=num, column=3)
    ifs.grid(row=num, column=4)
    fs.grid(row=num, column=5)
    elev.grid(row=num, column=6)
    desc.grid(row=num, column=7, padx=5)


def top_descriptions():
    point = Label(root, text="Point")
    bs = Label(root, text="BS")
    hi = Label(root, text="HI")
    ifs = Label(root, text="IFS")
    fs = Label(root, text="FS")
    elev = Label(root, text="Elevation")
    desc = Label(root, text="Description", padx=5)

    point.grid(row=0, column=1)
    bs.grid(row=0, column=2)
    hi.grid(row=0, column=3)
    ifs.grid(row=0, column=4)
    fs.grid(row=0, column=5)
    elev.grid(row=0, column=6)
    desc.grid(row=0, column=7)


def buttons():
    new_line = Button(root, text="+", padx=1, pady=1, command=lambda: add_row(count))
    new_line.grid(row=1, column=0)

    new_line = Button(root, text="-", padx=2, pady=1, command=lambda: remove_row())
    new_line.grid(row=2, column=0)


def add_row(amt):
    global count
    for i in range(amt):
        table(count)
    count += 1


def remove_row():
    return


def default_grid_size():
    for i in range(default_rows_num):
        table(i + 1)


top_descriptions()
buttons()
default_grid_size()

root.mainloop()
