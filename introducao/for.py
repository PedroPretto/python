#No python o for funciona como um iterador

lista = [1,2,3,4,5,6,7,8,9]

for item in lista:
    print(item)
    print(item * 2)
    print(item * 3)

for item in lista:
    if((item % 2) == 0):
        print("par")
    else:
        print("impar")

soma = 0

for item in lista:
    soma += item

print(soma)

string = 'Isso e uma string'

for char in string:
    print(char)

tupla = (1, 2, 3, 4, 5)

for t in tupla:
    print(t)


tupla_lista = [(1, 2), (2, 3), (3, 4)]

for (t1, t2) in tupla_lista:
    print(t1*t2)


dicti = {'k1':1, 'k2':2, 'k3':3}

for key in dicti:
    print(key)

for value in dicti.items():
    print(value)

for (key, value) in dicti.items():
    print(value)

