from klase import Kupac
from fajlovi import sacuvaj_kupce, ucitaj_kupce, ucitaj_prodavce

CONST_PUTANJA_KUPCI = 'kupci.txt'
CONST_PUTANJA_PRODAVCI = 'prodavci.txt'

def registruj_novog_kupca(kupci):
    print("________________REGISTRACIJA________________\n")     
    ime = input("Unesite ime: ").strip()
    prezime = input("Unesite prezime: ").strip()

    # validacija emaila
    email = input("Unesite email: ").strip()
    while "@" not in email:
        print("Email nije validan. Pokusajte ponovo.")
        email = input("Unesite email: ").strip() 

    # validacija sifre
    sifra = input("Unesite sifru (min 5 karaktera): ").strip()
    while len(sifra) < 5:
        print("Sifra mora imati bar 5 karaktera. Pokusajte ponovo.")
        sifra = input("Unesite sifru (min 5 karaktera): ").strip()                       
    
    # novi ID
    new_id = len(kupci) + 1

    # kreiramo kupca
    novi_kupac = Kupac(new_id, ime, prezime, email, sifra)
    kupci.append(novi_kupac)

    # snimamo u fajl
    sacuvaj_kupce(CONST_PUTANJA_KUPCI, kupci)
    return kupci

def uloguj_se():
    print("________________LOGOVANJE________________\n")     
    povratna_vrednost = -1
    # validacija emaila
    email = input("Unesite email: ").strip()
    while "@" not in email:
        print("Email nije validan. Pokusajte ponovo.")
        email = input("Unesite email: ").strip() 

    # validacija sifre
    sifra = input("Unesite sifru (min 5 karaktera): ").strip()
    while len(sifra) < 5:
        print("Sifra mora imati bar 5 karaktera. Pokusajte ponovo.")
        sifra = input("Unesite sifru (min 5 karaktera): ").strip()       

    kupci = ucitaj_kupce(CONST_PUTANJA_KUPCI)
    prodavci = ucitaj_prodavce(CONST_PUTANJA_PRODAVCI)

    for kupac in kupci:
        if kupac.email == email and kupac.sifra.rstrip("\n") == sifra:
            povratna_vrednost = 0
            return povratna_vrednost, kupac.id
        
    for prod in prodavci:
        if prod.email == email and prod.sifra ==sifra:
            povratna_vrednost = 1
            return povratna_vrednost, prod.id
    
    return povratna_vrednost,0