import random 
a = int(input("Введите размерность 1 массива: "))
b = int(input("Введите размерность 2 массива: "))
massa = []
massb = []

for l in range(a):
    massa.append(random.randint(0,10))

for t in range(b):
    massb.append(random.randint(0,15))

for k in set(massb):
    if k in massa:
        print(k)