a = 1
b = 1

if a == 2:
    a += 10

print(a)

a = [10, 4, 5, 3.5, 9]

for nota in a:
    if nota >= 9:
        print('Aprovado')
    
    elif nota >= 7:
        print('Recuperacao')
    
    else:
        print('Reprovado')