import sys
zdanie = input("Podaj zdanie: ")

print("Ilość słów: " + str(len(zdanie.strip().split())))
sys.stdout.write('Wprowadz liczbe (a)')
a=sys.stdin.readline()
a=int(a)
sys.stdout.write('Wprowadz liczbe (b)')
b=sys.stdin.readline()
b=int(b)
sys.stdout.write('Wprowadz liczbe (c)')
c=sys.stdin.readline()
c=int(c)

print(f"Wynik {a}^{b} + {c} = {a ** b + c}")

napis = input("Podaj napis: ")
napis = napis.lower().replace(" ", "")

if napis == napis[::-1]:
    print("Napis jest palindromem")
else:
    print("Napis nie jest palindromem")

n = 1000
x=0
for i in range(2, n + 1):
    suma = 0
    for j in range(1, i):
        if i % j == 0:
            suma += j
    if suma==i:
        x+=1
print(f"Liczba znalezionych liczb doskonałych: {x}")

tablica = [3, 4.5, 6, 7.2, 9.8, 10]

for k in range(len(tablica)):
    tablica[k] = tablica[k] ** 2
    k+=1

print(tablica)

lista= []
licz = 0
while licz < 10:
    number = int(input("Podaj liczbę: "))

    if number % 2 == 0:
        lista.append(number)
        licz += 1
    else:
        licz += 1

print("Parzyste liczby:", lista)

lista2 = [1, 'a', 1, 'b', 1, 'c', 3, 'a', 4, 'b', 5]

slownik = {}

for item in lista2:
    if item in slownik:
         slownik[item] += 1
    else:
        slownik[item] = 1

print("Słownik przed usunięciem")
print(slownik)

for klucz in list(slownik.keys()):
    if not isinstance(klucz, (int, float)):
        del slownik[klucz]

print("\nSłownik po usunięciu")
print(slownik)