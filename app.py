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
