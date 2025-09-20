from klase import Kupac, Narudzbina, Prodavac, Proizvod
from datetime import datetime

CONST_PUTANJA_PROIZVODI = 'tabela_proizvoda.txt'
CONST_PUTANJA_KUPCI = 'kupci.txt'

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
def ispisi_ime():
    print("nemanja mitrovic")

def sacuvaj_narudzbinu(putanja, narudzbina):
    """Snima sve narudzbine, a ovu sa istim ID-jem zamenjuje novom."""
    narudzbine = ucitaj_narudzbine(putanja)
    linije = []

    for n in narudzbine:
        if n.id == narudzbina.id:  # zameni
            proizvodi_str = ",".join(str(p.id) for p in narudzbina.proizvodi)
            linija = f"{n.id}|{narudzbina.vreme_porucivanja}|{narudzbina.status}|{narudzbina.kupac.id}|{narudzbina.ukupnaCena}|{proizvodi_str}"
        else:  # ostale narudzbine piši kako jesu
            proizvodi_str = ",".join(str(p.id) for p in n.proizvodi)
            linija = f"{n.id}|{n.vreme_porucivanja}|{n.status}|{n.kupac.id}|{n.ukupnaCena}|{proizvodi_str}"
        linije.append(linija)

    with open(putanja, "w") as fajl:
        fajl.write("\n".join(linije))

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

def ucitaj_proizvode(putanja):
    proizvodi = []
    fajl =  open(putanja, 'r')
    linije = fajl.readlines()
    for linija in linije:
        podeljena_linija = linija.split("|")
        id = podeljena_linija[0]
        vrsta = podeljena_linija[1]
        ukus = podeljena_linija[2]
        naziv = podeljena_linija[3]
        vreme_pripreme = podeljena_linija[4]
        cena = podeljena_linija[5]

        proizvod = Proizvod(id,vrsta, ukus, naziv, vreme_pripreme, cena)
        proizvodi.append(proizvod)
    fajl.close()
    return proizvodi

def ucitaj_narudzbine(putanja):
    narudzbine = []
    with open(putanja, 'r') as fajl:
        linije = fajl.readlines()

    kupci = ucitaj_kupce(CONST_PUTANJA_KUPCI)
    proizvodi = ucitaj_proizvode(CONST_PUTANJA_PROIZVODI)

    for linija in linije:
        podeljena_linija = linija.strip().split("|")
        id = int(podeljena_linija[0])
        vreme_porucivanja = datetime.strptime(podeljena_linija[1], "%Y-%m-%d").date()
        status = podeljena_linija[2]
        kupac_id = podeljena_linija[3]
        ukupna_cena = int(podeljena_linija[4])

        # pronađi kupca
        kupac = None
        for k in kupci:
            if str(k.id) == str(kupac_id) or k.ime == kupac_id:
                kupac = k
                break

        # pronađi proizvode
        proizvodi_narudzbine = podeljena_linija[5].split(',')
        svi_pro = []
        for pid in proizvodi_narudzbine:
            for p in proizvodi:
                if str(p.id) == pid:
                    svi_pro.append(p)

        narudzbina = Narudzbina(id, vreme_porucivanja, kupac, svi_pro)
        narudzbina.status = status
        narudzbina.ukupnaCena = ukupna_cena

        narudzbine.append(narudzbina)

    return narudzbine