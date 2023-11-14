import numpy as np

print("------1. Tehtävät------")
print("1.1 Muunna asteiksi")

a = 2.493
b = 0.911

ans1 = round(np.degrees(a), 2)
ans2 = round(np.degrees(b), 2)

print(f" a) 2,493 rad = {ans1} astetta   b) 0,911 rad = {ans2} astetta.")

print("\n1.2 Muunna radiaaneiksi")
c = 137.7
d = 62.3

ans3 = round(np.radians(c), 2)
ans4 = round(np.radians(d), 2)

print(f" a) 137,7 astetta = {ans3} rad   b) 62,3 = {ans4} rad.")

kulmien_asteet = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]

kulmat_radiaaneina = np.radians(kulmien_asteet)
kulmat_radiaaneina_lyhennetty = np.round(kulmat_radiaaneina, decimals=2)

kulmat_degrees = np.array(kulmien_asteet)

taulukko = np.column_stack((kulmat_degrees, kulmat_radiaaneina_lyhennetty))

print("\n3. Laadi taulukko, josta esittää seuraavat kulmat radiaaneina:"
      "\nKulmat asteina ja radiaaneina:"
      "\n|  Asteet | Radiaanit  |"
      "\n|---------|------------|")
for rivi in taulukko:
    print(f"| {rivi[0]:<7} | {rivi[1]:<10} |")

print("\n------2. Tehtävät--------")
print("2.1 Suorakulmaisen kolmion kateetit ovat 1,6 m ja 2,3 m. Kuinka pitkä on hypotenuusa?")

e = 1.6
f = 2.3

hypotenuusa = np.hypot(e, f)
print(f"1,6^2 + 2,3^2 = {hypotenuusa:.2f}^2")

print("\n2.3 Suorakulmion lävistäjä on 6,4 m ja sivujen pituuksien suhde 3:2."
      "Kuinka pitkiä ovat suorakulmion sivut?")
print("Näillä tiedoilla lausekkeesta tulee (3x)^2 + (2x)^2 = 6,4^2")
halkaisija = 6.4
suhde = np.array([3, 2])

x_squared = halkaisija**2 / (suhde[0]**2 + suhde[1]**2)
x = np.sqrt(x_squared)

sivu1 = suhde[0] * x
sivu2 = suhde[1] * x

print(f"Suorakulmion sivut ovat {sivu1:.2f} m ja {sivu2:.2f} m.")

print("\n------3. Tehtävät-----------")
print("3.1 Ratkaise suorakulmainen kolmio, kun alfa = 43,3 astetta ja a = 17,5mm")

alfa, kateetti_a = 43.3, 17.5

alfa_rad = np.radians(alfa)
hypotenuusa2 = kateetti_a / np.sin(alfa_rad)
kateetti_b = kateetti_a / np.tan(alfa_rad)
beeta_kulma = 180-90-43.3

print(f"Hyotenuusan pituus on {hypotenuusa2:.2f}mm,"
      f" kateetti b:n pituus on {kateetti_b:.2f}mm"
      f" ja beeta kulma on {beeta_kulma} astetta.")

print("\n3.1 Ratkaise suorakulmainen kolmio, kun beeta = 62,4 astetta ja c = 112 metriä.")
beeta, hypotenuusa3 = 62.4, 112
alfa2 = 180-90-62.4
beeta_rad = np.radians(beeta)
kateetti_a2 = hypotenuusa3 * np.cos(beeta_rad)
kateetti_b2 = hypotenuusa3 * np.sin(beeta_rad)

print(f"Kateetti a:n pituus on {kateetti_a2:.2f}mm,"
      f" kateetti b:n pituus on {kateetti_b2:.2f}mm"
      f" ja alfa kulma on {alfa2} astetta.")

print("\n3.2 Nopeudella 950 km/h lentänyt lentokone ylitti havaintopaikan ja näkyi 45 s myöhemmin "
      "35° korkeuskulmassa. Kuinka korkealla lentokone lensi?")
alfa3 = 35
kateetti_b3 = 950

x = (45/3600) * kateetti_b3
print(f"Kone on lentänyt 45s sekunnin aikana {x} kilometriä")

alfa3_rad = np.radians(alfa3)
kateetti_a3 = x * np.tan(alfa3_rad)

print(f"{kateetti_a3:.2f} kilometrin korkeudessa.")
