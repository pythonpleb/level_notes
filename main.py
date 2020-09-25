from tkinter import *
from Row import Row
from Col import Col

root = Tk()
root.title("Level Notes")

default_rows_num = 5
count = default_rows_num + 1

rows = []
cols = []


def table(num):
    point = Entry(root, borderwidth=3)
    bs = Entry(root, borderwidth=3)
    hi = Entry(root, borderwidth=3)
    ifs = Entry(root, borderwidth=3)
    fs = Entry(root, borderwidth=3)
    elev = Entry(root, borderwidth=3)
    desc = Entry(root, borderwidth=3)

    line = Row([point, bs, hi, ifs, fs, elev, desc])
    rows.append(line)

    column = Col(point, bs, hi, ifs, fs, elev, desc)
    cols.append(column)

    point.grid(row=num, column=1)
    bs.grid(row=num, column=2)
    hi.grid(row=num, column=3)
    ifs.grid(row=num, column=4)
    fs.grid(row=num, column=5)
    elev.grid(row=num, column=6)
    desc.grid(row=num, column=7, padx=5)

    # testing hi
    # elev.insert(0, 200)
    # bs.insert(0, 10)


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
    # TODO: fix button sizes
    new_line = Button(root, text="+", padx=2, pady=1, command=add_row)
    new_line.grid(row=1, column=0)

    new_line = Button(root, text="-", padx=3, pady=1, command=remove_row)
    new_line.grid(row=2, column=0)


def add_row():
    global count
    count += 1
    table(count)


def remove_row():
    global count
    if len(rows) < 3:  # make it a minimum of 2 rows
        return
    else:
        rows[len(rows) - 1].delete()
        rows.pop()
        count -= 1


def default_grid_size():
    for i in range(default_rows_num):
        table(i + 1)


def calculate():
    # elev - bs = hi
    # hi + fs = elev
    # hi + ifs = elev
    print(cols)
    return


top_descriptions()
buttons()
calculate()
default_grid_size()

root.mainloop()
