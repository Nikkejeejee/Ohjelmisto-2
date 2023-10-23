import random
from tabulate import tabulate


class auto():
    def __init__(self, rekisteri, hnopeus, thnopeus, kmatka):
        self.rekisteri = rekisteri
        self.hnopeus = hnopeus
        self.thnopeus = thnopeus
        self.kmatka = kmatka

    def kiihdyta(self, muutos):
        self.thnopeus += muutos
        if self.thnopeus > self.hnopeus:
            self.thnopeus = self.hnopeus
        if self.thnopeus < 0:
            self.thnopeus = 0

    def kulje(self, tuntimaara):
        self.kmatka += (tuntimaara * self.thnopeus)


autotalli = []

for kierros in range(10):
    auton_muodostus = auto(f'ABC-{kierros + 1}', random.randint(100, 200), 0, 0)
    autotalli.append(auton_muodostus)

kierros = 0

while True:
    kierros += 1
    if auton_muodostus.kmatka >= 10000:
        break
    for auton_muodostus in autotalli:
        auton_muodostus.kiihdyta(random.randint(-10, 15))
        auton_muodostus.kulje(1)

# kisojen_maara

yhteenveto = []
for auton_muodostus in autotalli:
    yhteenveto.append(
        (auton_muodostus.rekisteri, auton_muodostus.hnopeus, auton_muodostus.thnopeus, auton_muodostus.kmatka, kierros))

print(tabulate(yhteenveto,
               headers=['Rekisteri', 'Huippunopeus', 'Tämänhetkinen nopeus', 'Kuljettumatka', 'Kisojen määrä'],
               tablefmt='double_grid'))
