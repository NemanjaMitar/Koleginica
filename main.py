from klase import Osoba, Kupac, Narudzbina, Prodavac, Proizvod
from fajlovi import ucitaj_kupce,sacuvaj_kupce
from registacija import registruj_novog_kupca, CONST_PUTANJA_KUPCI, uloguj_se
from meniji import kupac_meni, prodavac_meni

if __name__ == "__main__":
    # Ucitaj kupce
    kupci = ucitaj_kupce(CONST_PUTANJA_KUPCI)

    while True:
        print("________PROGRAM ZA PORUCIVANJE HRANE________\n")
        print("1 -> Gasenje aplikacije")
        print("2 -> Registracija novog kupca")
        print("3 -> Logovanje")
        print("____________________________________________")
        izbor = input("Odaberite opciju: ").strip()

        if izbor == "1":
            print("Gašenje aplikacije...")
            sacuvaj_kupce(CONST_PUTANJA_KUPCI, kupci)
            exit()
        elif izbor == "2":
            kupci = registruj_novog_kupca(kupci)
            # nakon registracije opet nudimo meni za neulogovanog korisnika
            print("Vraćate se u meni za neulogovanog korisnika...")
        elif izbor == "3":
            uloga,id = uloguj_se()
            if uloga == -1:
                continue
            elif uloga == 1: # Prodavac
                prodavac_meni(id)
            elif uloga == 0: # Kupac
                kupac_meni(id)
        else:
            sacuvaj_kupce(CONST_PUTANJA_KUPCI, kupci)
            exit()