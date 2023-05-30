import datetime

class Zaklad:
  def __init__(self, miejsce, stawka, kurs):
    self.miejsce = miejsce
    self.stawka = stawka
    self.kurs = kurs
    self.data = datetime.datetime.now()
    
class Bukmacher:
  def __init__(self):
    self.zakłady = []
    
  def dodaj_zaklad(self, zaklad):
    self.zaklady.append(zaklad)
    
  def oblicz_wypłate(self, stawka, kurs):
    wygrana = stawka * kurs
    return wygrana

  def miejsce_zakladu(self):
    while True:
      try: 
        miejsce = int(input("Wybierz numer miejsca zakladu (1, 2, 3, 4, 5)"))
        if miejsce < 1:
          print("Wybierz poprawny numer miejsca!")
        else:
          return miejsce
      except ValueError:
        print("Podaj poprawny numer miejsca!")
