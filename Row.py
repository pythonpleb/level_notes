class Row:

    def __init__(self, entries):
        self.entries = entries

    def delete(self):
        for entry in self.entries:
            entry.grid_forget()
