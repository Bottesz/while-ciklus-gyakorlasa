"""1. Írjuk ki a számokat 0-150-ig páros számokat!"""

def feladat1():
    print(" 1.Feladat ")
    szam = 0
    while szam <= 150:
        if szam % 2 == 0:
            print(szam, end="")

        if szam == 150:
            print("", end=" ")
        else:
            print("", end=",")
        szam += 2


"""Számold meg 10 bekért szám esetében a 3-mal osztható számokat!"""

def feladat2():
    print(" 2. Feladat ")
    szam1 = 0
    oszthatoszamok= 0
    i:int = 0
    while i < 10:
        szambekeres = int(input(f"Kérem, adjon meg egy számot ({i + 1}. szám): "))

        if szambekeres  % 3 == 0:
            oszthatoszamok += 1


        i += 1

    print(f"Az 1-10. bekért számok közül {oszthatoszamok} darab osztható 3-mal.")

"""Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!"""

def feladat3():
    print(" 3. Feladat ")
    szambekeres = int(input("Kérem, adjon meg egy számot: "))
    while not (100 > szambekeres >= 10 and (szambekeres % 2 ==0)):
        print("Kétjegyű páros számot kell megadni")
        szambekeres:int =int(input("Kérem, adjon meg egy számot: "))
    print(f"A {szambekeres} kétjegyű páros szám.")


"""Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!"""
def  feladat4():
    print("4. Feladat")
    szambekeres: int = int(input("Adjon megy egy kétjegyű páros számot:"))
    while not ((100 > szambekeres >= 10 or szambekeres <= -10) and szambekeres % 2 == 0):
        szambekeres: int = int(input("Kérem adjon meg egy másik számot"))
    print(f"A {szambekeres} egy kétjegyű páros szám")

"""Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk"""

def feladat5():
    print("5. Feladat")
    szambekeres: int = int(input("Adjon meg egy pozitív páratlan számot:"))
    while not (szambekeres >= 0 and szambekeres % 2 == 1):
        szambekeres: int = int(input("Pozitív páratlan szám kell!:"))
    print(f"A {szambekeres} pozitív páratlan szám!")

"""Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz"""
def feladat6():
    print("6. Feladat")
    szambekeres: int = int(input("Adjon meg egy 3mal oszthato vagy négyzetszámot:"))
    while not (szambekeres % 3 == 0 or (szambekeres**0.5.is_integer())):
        szambekeres: int = int(input("3mal oszthato vagy négyzetszám kell:"))
    print(f"A {szambekeres} oszthato3mal vagy négyzetszám")

"""Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!"""

def feladat7():
    print("7. Feladat")
    szambekeres1:float = int(input("Adja meg az első oldalát:"))
    szambekeres2:float = int(input("Adja meg a második oldalát:"))
    szambekeres3:float = int(input("Adja meg a harmadik oldalát:"))
    while not (szambekeres1 + szambekeres2 > szambekeres3 and szambekeres1 + szambekeres3 > szambekeres2 and szambekeres2 + szambekeres3 > szambekeres1):
     szambekeres1 = float(input("Kérem, adjon meg az első oldal hosszát: "))
     szambekeres2 = float(input("Kérem, adjon meg a második oldal hosszát: "))
     szambekeres3 = float(input("Kérem, adjon meg a harmadik oldal hosszát: "))
     print("Ezek az oldalak alkothatnak egy háromszöget.")









