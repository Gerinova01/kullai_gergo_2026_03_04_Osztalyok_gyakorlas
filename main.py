from auto import Auto
import random

auto1 = Auto("Toyota", "Yaris", 2008)
auto2 = Auto("Ford", "Focus", 2018)
auto3 = Auto("Volvo", "s60", 2006)
auto4 = Auto("Alfa Romeo", "Giulia", 2007)
auto5 = Auto("Chevrolet", "Lacetti", 2017)

# auto1.gyorsit(150)
# auto1.fekez(30)
# print(auto1)

autok = [auto1, auto2, auto3, auto4, auto5]
for auto in autok:
    print(auto)

print("\nGyorsít\n")
for auto in autok:
    auto.gyorsit(random.randint(30, 150))
    print(auto)

autok_szama = len(autok)
ossz_eletkor = 0
for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    ossz_eletkor += kor

atlag_eletkor = ossz_eletkor / autok_szama
print(f"Az autók átlagéletkora {atlag_eletkor} év.")

legöregebb = autok[0]
for auto in autok:
    if auto.gyartasi_ev < legöregebb.gyartasi_ev:
        legöregebb = auto

legöregebb_auto = 2026 - legöregebb.gyartasi_ev
print(f"A legöregebb auto: {legöregebb.marka} {legöregebb.tipus} {legöregebb.gyartasi_ev} életkora {legöregebb_auto} év.")


gyartasi_evek = [auto.gyartasi_ev for auto in autok]

for auto in autok:
    if auto.gyartasi_ev == min(gyartasi_evek):
        eletkora = 2026 - auto.gyartasi_ev
        print(f"A legöregebb auti {auto} ami {eletkora} éves.")