from klase import Osoba, Kupac, Narudzbina, Prodavac, Proizvod
from fajlovi import sacuvaj_narudzbinu, ucitaj_kupce, sacuvaj_kupce, ucitaj_proizvode, ucitaj_narudzbine
from registacija import registruj_novog_kupca, CONST_PUTANJA_KUPCI, uloguj_se
from datetime import datetime
from klase import CONST_STATUS, CONST_UKUS, CONST_VRSTA

CONST_PUTANJA_PROIZVODI = 'tabela_proizvoda.txt'
CONST_PUTANJA_NARUDZBINE = 'narudzbine.txt'

def kupac_meni(id):
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
            proizvod = input("Koji proizvod zelite da pretrazite : ")
            pretrazi_proizvod(proizvod)
        elif izbor == "4":
            prikazi_narudzbine(id)

        elif izbor == "5":
            print("Vrsta\t|Ukus\t|Naziv\t|Vreme Pripreme\t|Cena")
            print("----------------------------------------------")
            proizvodi = ucitaj_proizvode(CONST_PUTANJA_PROIZVODI)
            for p in proizvodi:
                print_proizvod(p)
            print("----------------------------------------------")
            ulaz = input("Unesite ID proizvoda koji zelite da narucite (Unesite 'x' ako zelite da prekinete) : ")
            if ulaz == 'x':
                continue
            naruci(ulaz,id)
        else:
            sacuvaj_kupce(CONST_PUTANJA_KUPCI, kupci)
            exit()

def prikazi_narudzbine(id=None):
    if id:
        fajl = open('narudzbine.txt', 'r')
        linije = fajl.readlines()
        for linija in linije:
            splitovana_linija = linija.split('|')
            
            if splitovana_linija[3] == id:
                print(f'id : {splitovana_linija[0]}')         
                print(f'vreme : {splitovana_linija[1]}')
                print(f'status : {splitovana_linija[2]}')
                kupci = ucitaj_kupce(CONST_PUTANJA_KUPCI)
                for k in kupci:
                    if k.id == id:
                        print(f'kupac : {k.ime}')
                print(f'cena: {splitovana_linija[4]}')
                proizvodi = ucitaj_proizvode(CONST_PUTANJA_PROIZVODI)
                id_proizvoda = splitovana_linija[5].split(',')
                id_proizvoda[-1] = id_proizvoda[-1].rstrip('\n')
                nazivi = []
                for idp in id_proizvoda:
                    for p in proizvodi:
                        if p.id == idp:
                            nazivi.append(p.naziv)
                print("Proizvodi : " + ",".join(nazivi))
                print("____________________________________________")
    else:
        fajl = open('narudzbine.txt', 'r')
        linije = fajl.readlines()
        for linija in linije:
            splitovana_linija = linija.split('|')
            print(f'id : {splitovana_linija[0]}')         
            print(f'vreme : {splitovana_linija[1]}')
            print(f'status : {splitovana_linija[2]}')
            kupci = ucitaj_kupce(CONST_PUTANJA_KUPCI)
            for k in kupci:
                if k.id == id:
                    print(f'kupac : {k.ime}')
            print(f'cena: {splitovana_linija[4]}')
            proizvodi = ucitaj_proizvode(CONST_PUTANJA_PROIZVODI)
            id_proizvoda = splitovana_linija[5].split(',')
            id_proizvoda[-1] = id_proizvoda[-1].rstrip('\n')
            nazivi = []
            for idp in id_proizvoda:
                for p in proizvodi:
                        if p.id == idp:
                            nazivi.append(p.naziv)
            print("Proizvodi : " + ",".join(nazivi))
            print("____________________________________________")
            
            

def pretrazi_proizvod(proizvod):
    proizvodi = ucitaj_proizvode(CONST_PUTANJA_PROIZVODI)
    print("ID\t|Vrsta\t|Ukus\t|Naziv\t|Vreme Pripreme\t|Cena")
    print("----------------------------------------------")
    for p in proizvodi:
        if p.naziv == proizvod or p.vrsta == proizvod or p.ukus == proizvod:
            print_proizvod(p)

def pregledaj_proizvod(proizvod):
    proizvodi = ucitaj_proizvode(CONST_PUTANJA_PROIZVODI)
    print("Id\t|Vrsta\t|Ukus\t|Naziv\t\t|Vreme Pripreme\t|Cena")
    print("----------------------------------------------")
    for p in proizvodi:
        if p.naziv == proizvod:
            print_proizvod(p)
    
def print_proizvod(p):
    print(f'{p.id}\t|{p.vrsta}\t|{p.ukus}\t|{p.naziv}\t|{p.vreme_pripreme}\t\t|{p.cena} ')

def naruci(proizvodi, id_kupca): # '1,2,3'
    fajl = open(CONST_PUTANJA_NARUDZBINE,'r')
    linije = fajl.readlines()
    id = len(linije)  + 1
    vreme_porucivanja = datetime.now()
    vreme_porucivanja = vreme_porucivanja.date()
    status = CONST_STATUS[0]
    kupac = id_kupca
    ukupna_cena = 0
    lista_proizvoda = proizvodi.rstrip(' ').split(',')
    prava_lista = ''
    for p in lista_proizvoda:
        prava_lista += p + ','
    prava_lista = prava_lista.rstrip(',')
    proizvodi = ucitaj_proizvode(CONST_PUTANJA_PROIZVODI)
    for p in lista_proizvoda:
        for pro in proizvodi:
            if pro.id == p:
                ukupna_cena += int(pro.cena)
    prefix = "\n" if linije else ""
    linija = f'{prefix}{id}|{vreme_porucivanja}|{status}|{kupac}|{ukupna_cena}|{prava_lista}'

    fajl.close()

    fajl = open(CONST_PUTANJA_NARUDZBINE, 'a')
    fajl.write(linija)
    fajl.close()

def prodavac_meni(id):
    kupci = ucitaj_kupce(CONST_PUTANJA_KUPCI)

    while True:
        print("______________MENI ZA PRODAVCA_____________\n")
        print("1 -> Gasenje aplikacije")
        print("2 -> Tabelarni pregled proizvoda")
        print("3 -> Pregled narudzbina")
        print("4 -> Promena statusa narudzbine")
        print("5 -> Dodavanje proizvodoa")
        print("6 -> Prikaz 3 najprodavanija proizvoda")
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
            
           prikazi_narudzbine()
        elif izbor == "4":
            prikazi_narudzbine()
            id_narudzbine = input("Unesite ID narudzbine kojoj hocete da promenite status: ")

            # konverzija u int da se poklapa sa n.id
            try:
                id_narudzbine = int(id_narudzbine)
            except ValueError:
                print("ID mora biti broj!")
            else:
                novi_status = input("Unesite novi status: ")
                while novi_status not in CONST_STATUS:
                    novi_status = input("Greška pri kucanju, unesite ponovo: ")

                narudzbine = ucitaj_narudzbine(CONST_PUTANJA_NARUDZBINE)
                nova_nar = None
                for n in narudzbine:
                    if n.id == id_narudzbine:
                        n.status = novi_status
                        nova_nar = n
                        break

                if nova_nar:
                    sacuvaj_narudzbinu(CONST_PUTANJA_NARUDZBINE, nova_nar)
                    print("Status uspešno promenjen!")
                else:
                    print("Narudzbina sa tim ID-jem nije pronađena.")
        elif izbor == '5':
            dodaj_novi_proizvod()
        elif izbor == '6':
            narudzbine = ucitaj_narudzbine(CONST_PUTANJA_NARUDZBINE)
            artikli = {}
            for narudzbina in narudzbine:
                for proizvod in narudzbina.proizvodi:
                    if proizvod not in artikli:
                        artikli[proizvod] = 1
                    else:
                        artikli[proizvod] += 1
            top3 = sorted(artikli.items(), key=lambda x: x[1], reverse=True)[:3]
            print("Top 3 najprodavanija proizvoda:")
            for proizvod, broj in top3:
                print(f"- {proizvod.naziv} (prodato {broj} puta)")
        else:
            sacuvaj_kupce(CONST_PUTANJA_KUPCI, kupci)
            exit()


def dodaj_novi_proizvod():
    vrsta = input("Unesite vrstu novog proizvoda : ")
    if vrsta not in CONST_VRSTA:
        vrsta = input("Greska pri unosu, unesite vrstu novog proizvoda : ")
    
    ukus = input("Unesite ukus novog proizvoda : ")
    if ukus not in CONST_UKUS:
        ukus = input("Greska pri unosu, unesite vrstu novog proizvoda : ")

    cena = int(input("Unesite cenu novog proizvoda : "))
    if cena < 0:
        cena = int(input("Greska pri unosu, unesite cenu vecu od 0 : "))

    vreme_pripreme = int(input("Unesite vreme pripreme novog proizvoda : "))
    if vreme_pripreme < 0:
        vreme_pripreme = int(input("Greska pri unosu, unesite vreme vecu od 0 : ")) 
    naziv = input("Unesite naziv proizvoda : ")

    fajl = open(CONST_PUTANJA_PROIZVODI, 'r')
    linije = fajl.readlines()
    idp = len(linije) + 1
    fajl.close()
    # Append (ne briše fajl)
    with open(CONST_PUTANJA_PROIZVODI, 'a', encoding="utf-8") as fajl:
        if len(linije) > 0 and not linije[-1].endswith("\n"):
            fajl.write("\n")  # dodaj newline ako poslednja linija nema
        fajl.write(f"{idp}|{vrsta}|{ukus}|{naziv}|{vreme_pripreme}|{cena}")