
class Napitak:

    lista_alkohola = []
    lista_sokova = []

    def __init__(self, naziv, kolicina):
        self.naziv = naziv
        self.kolicina = kolicina


    def __str__(self):
        return f"Naziv:  {self.naziv}  / Kolicina: {str(self.kolicina)}"

    @classmethod
    def info(cls):
        ukupno_alkohola = sum(pice.kolicina for pice in cls.lista_alkohola)
        ukupno_sokova = sum(pice.kolicina for pice in cls.lista_sokova)
        ukupno_pica = ukupno_sokova + ukupno_alkohola

        return f"Svega ukupno ima {ukupno_pica} napitaka\nOd toga {ukupno_alkohola} Alkohola\nI {ukupno_sokova} sokova"


class Alkohol(Napitak):

    def __init__(self, naziv, kolicina, postotak_alkohola):
        super().__init__(naziv, kolicina)
        self.postotak_alkohola = postotak_alkohola

        Napitak.lista_alkohola.append(self)

    def __str__(self):
        return Napitak.__str__(self) + " / Postotak alkohola: " + str(self.postotak_alkohola) + "%"

    @classmethod
    def info(cls):
        ukupno_alkohola = sum(pice.kolicina for pice in cls.lista_alkohola)
        return f"Ukupno ima {ukupno_alkohola} alkoholnih pica"



class Sok(Napitak):

    def __init__(self, naziv, kolicina, postotak_secera):
        super().__init__(naziv, kolicina)
        self.postotak_secera = postotak_secera

        Napitak.lista_sokova.append(self)



    def __str__(self):
        return Napitak.__str__(self) + " / Postotak secera: " + str(self.postotak_secera) + "%"

    @classmethod
    def info(cls):
        ukupno_sokova = sum(pice.kolicina for pice in cls.lista_sokova)
        return f"Ukupno ima {ukupno_sokova} sokova "



napitak1 = Alkohol("Nektar", 8, 5)
napitak2 = Alkohol("Tuborg", 20, 4.5)
napitak3 = Sok("Fanta", 15, 8 )
napitak4 = Sok("Sprite", 12, 9)
napitak5 = Alkohol("Rakija", 7, 30)

print(Napitak.lista_alkohola)


