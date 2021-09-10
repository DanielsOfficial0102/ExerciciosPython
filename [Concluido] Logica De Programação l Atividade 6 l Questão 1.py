#Atividade 06 - Lógica de Programação
#1. Faça uma programa que permita a exibição de Tabuada de um número qualquer a ser escolhido pelo usuário.


x = 1

y = int(input('Insira o Número : '))

if (y < 11):

    print ('Tabuada:',y)
    print('\n')

    while (x < 11):        

        print('{} x {:2} = {}'.format(y, x, y * x))

        x += 1

    y += 1

    print ('\n')

    print ('========================')

    print ('\n')


input('Pressione Enter Para Sair')
