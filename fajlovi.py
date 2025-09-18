from klase import Kupac, Prodavac

def sacuvaj_kupce(putanja, kupci):
    fajl =  open(putanja, 'w')
    linije = []
    for kupac in kupci:
        kupac.sifra = kupac.sifra.rstrip("\n") 
        linija  = str(kupac.id) + "|" + kupac.ime + "|" + kupac.prezime + "|" + kupac.email + "|" + kupac.sifra + '\n'
        linije.append(linija)
    fajl.writelines(linije)
    fajl.close()
    return


def ucitaj_kupce(putanja):
    kupci = []
    fajl =  open(putanja, 'r')
    linije = fajl.readlines()
    for linija in linije:
        podeljena_linija = linija.split("|")
        id = podeljena_linija[0]
        ime = podeljena_linija[1]
        prezime = podeljena_linija[2]
        email = podeljena_linija[3]
        sifra= podeljena_linija[4]
        kupac = Kupac(id, ime, prezime, email, sifra)
        kupci.append(kupac)
    fajl.close()
    return kupci

def ucitaj_prodavce(putanja):
    prodavci = []
    fajl =  open(putanja, 'r')
    linije = fajl.readlines()
    for linija in linije:
        podeljena_linija = linija.split("|")
        id = podeljena_linija[0]
        ime = podeljena_linija[1]
        prezime = podeljena_linija[2]
        email = podeljena_linija[3]
        sifra= podeljena_linija[4]
        godinaStaza = int(podeljena_linija[5])
        prodavac = Prodavac(id, ime, prezime, email, sifra, godinaStaza)
        prodavci.append(prodavac)
    fajl.close()
    return prodavci