x = []
for i in range(0,5):
    x.append(i)

x2 = [i for i in range(0,30)]
print(x2)

#criando lista de pares
pares = [i for i in range(0,20) if i % 2 == 0]
print(pares)

#compreensao com strings
lista = [letter for letter in 'word']
print(lista)


#conversao de celsius para fahrenheit

celsius = [0, 10, 15, 20, 30, 50, 100]
fahrenheit = [(temp * (9/5) + 32) for temp in celsius]

print(fahrenheit)