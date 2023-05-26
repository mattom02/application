import datetime

class Zaklad:
  def __init__(self, miejsce, stawka, kurs):
    self.miejsce = miejsce
    self.stawka = stawka
    self.kurs = kurs
    self.data = datetime.datetime.now()
