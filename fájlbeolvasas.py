from auto import Auto

autok = []
with open('adatok/autok.txt', 'r', encoding = 'utf-8' ) as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        if len(adatok) >= 4:
            marka, tipus, gyartasi_ev, fogyasztas = adatok
        auto = Auto(marka, tipus, int(gyartasi_ev), float(fogyasztas))
        autok.append(auto)

for auto in autok:
    print(auto)