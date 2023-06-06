import datetime

class Zaklad:
    def __init__(self, miejsce, stawka, kurs):
        self.miejsce = miejsce
        self.stawka = stawka
        self.kurs = kurs
        self.data = datetime.datetime.now()

class Bukmacher:
    def __init__(self):
        self.zaklady = []

    def dodaj_zaklad(self, zaklad):
        self.zaklady.append(zaklad)

    def oblicz_wyplate(self, stawka, kurs):
        wygrana = stawka * kurs
        return wygrana

    def miejsce_zakladu(self):
        while True:
            try:
                miejsce = int(input("Wybierz numer miejsca zakładu (1, 2, 3 itd.): "))
                if miejsce < 1:
                    print("Wybierz poprawny numer miejsca!")
                else:
                    return miejsce
            except ValueError:
                print("Podaj poprawny numer miejsca!")

    def miejsce_stawki(self):
        while True:
            try:
                stawka = float(input("Podaj stawkę zakładu: "))
                if stawka <= 0:
                    print("Stawka musi być większa od zera!")
                else:
                    return stawka
            except ValueError:
                print("Podaj poprawną stawkę!")

    def pobierz_kursy(self):
        kursy = []
        while True:
            try:
                ilosc_miejsc = int(input("Podaj ilość miejsc w zakładzie: "))
                if ilosc_miejsc < 2:
                    print("Podaj poprawną ilość miejsc!")
                else:
                    break
            except ValueError:
                print("Podaj poprawną ilość miejsc!")

        for i in range(ilosc_miejsc):
            while True:
                try:
                    kurs = float(input(f"Podaj kurs dla miejsca {i+1}: "))
                    if kurs <= 0:
                        print("Kurs musi być większy od zera!")
                    else:
                        kursy.append(kurs)
                        break
                except ValueError:
                    print("Podaj poprawny kurs!")
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
            print("Menu główne:")
            print("1. Dodaj zakład")
            print("2. Wyświetl historię zakładów")
            print("3. Wyjście")

            wybor = input("Wybierz opcję: ")
            if wybor == "1":
                kursy = self.pobierz_kursy()
                miejsce = self.miejsce_zakladu()
                stawka = self.miejsce_stawki()
                zaklad = Zaklad(miejsce, stawka, kursy[miejsce-1])
                wygrana = self.oblicz_wyplate(stawka, kursy[miejsce-1])
                self.dodaj_zaklad(zaklad)
                print(f"Zaklad dodany. Wygrana mozliwa w przypadku trafienia: {wygrana}")
            elif wybor == "2":
                self.wyswietl_historie()
            elif wybor == "3":
                print("Dziekujemy za skorzystanie z aplikacji.")
                break
            else:
                print("Wybierz poprawna opcje.")

if __name__=="__main__":
    bukmacher = Bukmacher()
    bukmacher.main_menu()
