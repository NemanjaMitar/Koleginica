from klase import Osoba, Kupac, Narudzbina, Prodavac, Proizvod
from fajlovi import ucitaj_kupce,sacuvaj_kupce
from registacija import registruj_novog_kupca, CONST_PUTANJA_KUPCI, uloguj_se

def kupac_meni():
    kupci = ucitaj_kupce(CONST_PUTANJA_KUPCI)

    while True:
        print("________________MENI ZA KUPCA_______________\n")
        print("1 -> Gasenje aplikacije")
        print("2 -> Tabelarni pregled proizvoda")
        print("3 -> Pretraga proizvoda")
        print("4 -> Pregled narudzbina")
        print("5 -> Narucivanje")
        print("____________________________________________")
        izbor = input("Odaberite opciju: ").strip()

        if izbor == "1":
            print("Gašenje aplikacije...")
            sacuvaj_kupce(CONST_PUTANJA_KUPCI, kupci)
            exit()
        elif izbor == "2":
            print("____________________________________________")
            proizvod = input("Koji proizvod zelite da prikazete : ")
            pregledaj_proizvod(proizvod)
        elif izbor == "3":
            uloga = uloguj_se()
            if uloga == -1:
                continue
            elif uloga == 1: # Prodavac
                print("Pozdrav prodavac")
            elif uloga == 0: # Kupac
                print("Pozdrav kupac")
        else:
            sacuvaj_kupce(CONST_PUTANJA_KUPCI, kupci)
            exit()

def pregledaj_proizvod(proizvod):
    return