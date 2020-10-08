my_list = [1,2,3]
print(my_list)

my_multi_list = [1,2.5,'Pedro']
print(my_multi_list)

print('string = ' + my_multi_list[2])

print(my_multi_list[1:]) # printar a lista a partir da posicao 1

print(my_multi_list[-1]) # printa o ultimo, de tras para frente E.g: -n

lista = my_list + my_multi_list # possivel somar listas

print(lista)

# metodos de lista

type(lista)
print(len(lista))

lista.append('mais um') #adiciona no final
print(lista)

lista.pop() #remove o ultimo
print(lista)

lista.pop(2) #remove no indice 2
print(lista)

lista.reverse() #inverte ordem
print(lista)