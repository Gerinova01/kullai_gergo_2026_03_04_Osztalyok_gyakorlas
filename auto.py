class Auto:
    def __init__(self, marka_, tipus_, gyartasi_ev_):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasi_ev = gyartasi_ev_

    def __str__(self):
        return f"{self.marka} {self.tipus} {self.gyartasi_ev}"