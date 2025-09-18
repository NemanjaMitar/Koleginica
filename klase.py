import datetime 

CONST_STATUS = ["naručeno", "u pripremi", "spremno", "dostavljeno"]
CONST_VRSTA = ["hrana", "pice"]
CONST_UKUS = ["slatko", "ljuto", "slano"]

class Osoba:
    def __init__(self, id=None, ime="", prezime="", email="", sifra=""):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        self.email = email
        self.sifra = sifra

class Kupac(Osoba):
    def __init__(self, id=None, ime="", prezime="", email="", sifra="", lista_narudzbina=None):
        super().__init__(id, ime, prezime, email, sifra)
        self.lista_narudzbina = lista_narudzbina 


class Prodavac(Osoba):
    def __init__(self, id=None, ime="", prezime="", email="", sifra="", godinaRadnogStaza=0):
        super().__init__(id, ime, prezime, email, sifra)
        self.godinaRadnogStaza = godinaRadnogStaza

class Narudzbina:
    def __init__(self, id=None, vreme_porucivanja=None, kupac=None, proizvodi=None):
        self.id = id
        if vreme_porucivanja :
            self.vreme_porucivanja = vreme_porucivanja     
        else:
            datetime.datetime.now()
        
        self.status = CONST_STATUS[0]  
        self.kupac = kupac
        self.proizvodi = proizvodi 
        
        self.ukupnaCena = 0
        for proizvod in proizvodi:
            self.ukupna_cena += proizvod.cena


class Proizvod:
    def __init__(self, id=None, vrsta=CONST_VRSTA[0], ukus=CONST_UKUS[0], naziv="", vreme_pripreme=0, cena=0, lista_narudzbina=None):
        self.id = id
        self.vrsta = vrsta          
        self.ukus = ukus            
        self.naziv = naziv
        self.vreme_pripreme = vreme_pripreme
        self.cena = cena
        self.lista_narudzbina = lista_narudzbina 

