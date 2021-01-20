#definindo uma funcao com docstring
def primeira_funcao():
    """
    printa ola mundo
    """
    print('Ola Mundo')
primeira_funcao()


#funcao com argumento
def somar(x,y):
    return x+y
resultado = somar(2,2)
print(resultado)

#numero primo
def primo(numero):
    """
    funcao para checar numero primo
    """
    for n in range(2, numero):
        if numero % n == 0:
            print('Nao eh primo')
            break

    print('Primo')

primo(2)