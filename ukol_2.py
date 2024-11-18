"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Daniel Sychra
email: daniel.sychra@gmail.com
"""


import random

def pozdrav_uzivatele():
    print("Vítejte ve hře Bulls and Cows!")
    print("Vaším úkolem je uhodnout tajné čtyřciferné číslo.")
    print("Číslice musí být unikátní a číslo nesmí začínat nulou.")
    print("Po každém pokusu vám řekneme, kolik máte bulls a cows.")
    print("1 bull znamená, že jste uhodli jak číslo, tak jeho umístění.")
    print("1 cow znamená, že jste uhodli číslo, ale ne jeho umístění.")
    print("Hodně štěstí!")

def vytvor_tajne_cislo():
    cisla = list(range(1, 10))
    random.shuffle(cisla)
    tajne_cislo = cisla[:4]
    return tajne_cislo

def ziskej_tip():
    while True:
        tip = input("Zadejte svůj tip: ")
        if len(tip) != 4:
            print("Tip musí mít přesně 4 číslice.")
            continue
        if not tip.isdigit():
            print("Tip musí obsahovat pouze číslice.")
            continue
        if len(set(tip)) != 4:
            print("Tip nesmí obsahovat duplicitní číslice.")
            continue
        if tip == '0':
            print("Tip nesmí začínat nulou.")
            continue
        return [int(cifra) for cifra in tip]

def vyhodnot_tip(tip, tajne_cislo):
    bulls = 0
    cows = 0
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1
    return bulls, cows

def main():
    pozdrav_uzivatele()
    tajne_cislo = vytvor_tajne_cislo()
    while True:
        tip = ziskej_tip()
        bulls, cows = vyhodnot_tip(tip, tajne_cislo)
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        if bulls == 4:
            print("Gratulujeme! Uhodli jste tajné číslo.")
            break

if __name__ == "__main__":
    main()


