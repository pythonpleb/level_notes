class Col:
    def __init__(self, point, bs, hi, ifs, fs, elev, desc):
        self.point = point
        self.bs = bs
        self.hi = hi
        self.fs = fs
        self.ifs = ifs
        self.elev = elev
        self.desc = desc

    def store_info(self, point, bs, hi, ifs, fs, elev, desc):
        self.point.append(point)
        self.bs.append(bs)
        self.hi.append(hi)
        self.fs.append(fs)
        self.ifs.append(ifs)
        self.elev.append(elev)
        self.desc.append(desc)

    def get_elev(self):
        for elev in self.elev:
            return elev.get()

    def get_bs(self):
        for bs in self.bs:
            return bs.get()

    def calc_hi(self):
        value1 = 0
        value2 = 0
        for e in self.elev:
            value1 += e.get_elev()

        for e in self.bs:
            value2 += e.get_bs()

        return value1 - value2
