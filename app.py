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
  
  def miejsce_stawki(self):
    while True:
      try:
        stawka = float(input("Podaj stawke zakładu: "))
        if syawka <= 0:
          print("Stawka musi być większa od zera!!!")
        else:
          return stawka
      except ValueError:
        print(" Podaj poprawną stawke")
        
  def pobierz_kursy(self):
    kursy = []
    while True:
        try:
          ilosc_miejsc = int(input("Podaj ilosc miejsc w zakladzie: ")
          if ilosc_miejsc < 2:
            print("Podaj poprawna ilosc miejsc!")
          else:
            break
        except ValueError:
            print("Podaj poprawna ilosc miejsc!")
                             
      for i in range(ilosc_miejsc):
          while True:
            try:
                kurs = float(input(f"Podaj kurs dla miejsca {i+1}: "))
                if kurs <= 0;
                    print("Kurs musi byc większy od zera!")
                else:
                    kursy.append(kurs)
                    break
              except ValueErtor:
                print ("Podaj poprawny kurs!") 
           return kursy
                             
    def wyswietl_historie(self):
        if not self.zaklady:
	          print("Brak zakładów w historii.")
	          return

        print("Historia zakładów:")
        for zaklad in self.zaklady:
            print(f"Miejsce: {zaklad.miejsce}")
	          print(f"Stawka: {zaklad.stawka}")
	          print(f"Kurs: {zaklad.kurs}")
	          print(f"Data: {zaklad.data}")
	          print()
                                  
                         
    def main_menu(self):
	while True:
			     
	    print("menu głowne: ")
	    print("1. Dodaj zakład")
	    print("2. Wyświetl historie zakładów"
            print("3. Wyjście")
		  
            wybor = input("wybierz opcje: "0)
	    if wybor == "1" :
		kursy = self.pobierz_kursy()
		  miejsce = self.miejsce_zakładu()
