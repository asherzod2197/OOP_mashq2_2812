class Kitob:
    def __init__(self, nomi, muallif, yil):
        self.nomi = nomi
        self.muallif = muallif
        self.yil = yil

    def malumot(self):
        return f"{self.nomi} | {self.muallif} | {self.yil}"


class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def chiqarish(self):
        if not self.kitoblar:
            print("Kitoblar yo‘q")
        else:
            for k in self.kitoblar:
                print(k.malumot())


kutubxona = Kutubxona()

kutubxona.qoshish(Kitob("Python asoslari", "A. Karimov", 2022))
kutubxona.qoshish(Kitob("Algoritmlar", "B. Aliyev", 2020))
kutubxona.qoshish(Kitob("Dasturlash", "S. Hasanov", 2023))

print("Kutubxona ro‘yxati:")
kutubxona.chiqarish()
