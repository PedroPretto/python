my_file = open('python.txt')


#metodos

print(my_file.read()) #le o conteudo

print(my_file.readline()) #vai ler a linha de onde o cursor parou (read le ate o final)

my_file.seek(0) #resetando o cursor

print(my_file.readline()) #agora sim

my_file.seek(0)

for line in my_file:
    print(line)
