class Bolt:
    def __init__(self,kosar: str):
        self.kosar = kosar

    def feladat_1(filepath: str) -> list:
        file = open(filepath,'r')
        vasarlok = []
        for sor in file:
            sor = sor.strip()
            if sor!= "F":
                vasarlok.append(sor)
            else:
                vasarlok.append(" ")
        print("1. feladat: A kosar.txt beolvasása.")
        file.close()
        return vasarlok


    def feladat_2(lista: list) -> None:
        szam = 0
        for i in lista:
            if i == " ":
                szam+=1
        print(f"2. feladat: {szam} alkalommal fizettek a pénztárnál.")


    def feladat_3(lista: list) -> None:
        i = 1
        szam = 1
        for j in lista:
            if j == " ":
                szam+=1
        print(f"2. feladat: {szam} alkalommal fizettek a pénztárnál.")
        while(True):
            sorszam = int(input("3. feladat: Adja meg a vásárlás sorszámát: "))
            if sorszam > 0 and sorszam < szam : break
            else: print("Hibás sorszám")


        Termekek = " "
        for temp in lista:
            if(temp == " "):
                i+=1
            elif i == sorszam:
                Termekek+=f"{temp}\n"
        print(f"A kosár tartalma: {Termekek}\n")


    def feladat_4(lista:list) -> None:
        aruk = []
        for i in lista:
            if i != " ":
                if i not in aruk:
                    aruk.append(i)
        while(True):
            termek = input("4. feladat: Kérek egy terméket: ")
            if termek not in aruk :
                print("Hibás termék")
            else: break


        sorszam = 1
        sorszam2 = 1
        osszesen = 0
        for j in lista:
            if j== termek:
                osszesen += 1
            if j == " ":
                sorszam2+=1


        for i in lista:
            if i == termek:
                print(f"Első vásárlás sorszáma: {sorszam}")
                break
            if i == " ":
                sorszam+=1
            if(sorszam > sorszam2):
                print("Nincs ilyen árú")
        reverselista = lista[::-1]

        for k in reverselista:
            if k == termek:
                print(f"utolsó vásárlás sorszáma: {sorszam2}")
                break
            if k == " ":
                sorszam2-=1
        print(f"Összesen ennyi alkalommal vásároltak belőle: {osszesen}")


    def feladat_5(lista:list,filepath: str) -> None:
        aruk = []
        for i in lista:
            if i != " ":
                if i not in aruk:
                    aruk.append(i)
        osszeg1 = 1000
        osszeg2 = 900
        osszeg3 = 800
        osszes = 0
        vasarlas = []
        for i in range(len(aruk)):
            vasarlas.append(0)

        file = open(filepath,"w")
        for j in lista:
            if j !=" ":
                if j == aruk[0]: vasarlas[0] += 1
                if j == aruk[1]: vasarlas[1] += 1
                if j == aruk[2]: vasarlas[2] += 1
                if j == aruk[3]: vasarlas[3] += 1
                if j == aruk[4]: vasarlas[4] += 1
                if j == aruk[5]: vasarlas[5] += 1
                if j == aruk[6]: vasarlas[6] += 1
                if j == aruk[7]: vasarlas[7] += 1
                if j == aruk[8]: vasarlas[8] += 1
            if j == " ":
                for k in vasarlas:
                    if k == 0 : osszes += 0
                    if k == 1 : osszes += osszeg1
                    if k == 2 : osszes += osszeg2 + osszeg1
                    if k >= 3 : osszes += osszeg1 + osszeg2 + osszeg3 + (k-3)*osszeg3
                file.write(f"{str(osszes)}\n")
                osszes = 0
                vasarlas.clear()
                for i in range(len(aruk)):
                    vasarlas.append(0)
        print("5. feladat:  A vásárlások összegének mentése a osszeg.txt fájlba")
        file.close()






