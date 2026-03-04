class Auto:

    def __init__(self, marka_, tipus_, gyartasi_ev_, uzemanyag_=50, fogyasztas_=7.5):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasi_ev = gyartasi_ev_
        self.sebesseg = 0
        self.uzemanyag = uzemanyag_
        self.fogyasztas = fogyasztas_

    def __str__(self):
        return f"{self.marka} {self.tipus} {self.gyartasi_ev}, sebesség = {self.sebesseg} km/h"
    
    def gyorsit(self, ertek):
        self.sebesseg += ertek
        if self.sebesseg > 200:
            self.sebesseg = 200

    def fekez(self, ertek):
        self.sebesseg -= ertek
        if self.sebesseg < 0:
            self.sebesseg = 0
    

    def tankol(self, mennyiseg):
        self.uzemanyag += mennyiseg
        if self.uzemanyag > 50:
            self.uzemanyag = 50