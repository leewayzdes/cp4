a = int(input("Введите размерность массива: "))
massiv = []
print("Введите элементы массива: ")

for i in range(a):
    massiv.append(float(input()))
m = max(massiv)

for g in range(a):
    if massiv[g] == m:
        index = g
        break
    
for d in range(index+1,a):
    massiv[d]=0

print("Полученный массив: ")
print(massiv)
