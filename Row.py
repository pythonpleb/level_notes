class Row:

    def __init__(self, entries):
        self.entries = entries
        self.point = []
        self.bs = []
        self.hi = []
        self.fs = []
        self.ifs = []
        self.desc = []

    def delete(self):
        for entry in self.entries:
            entry.grid_forget()
