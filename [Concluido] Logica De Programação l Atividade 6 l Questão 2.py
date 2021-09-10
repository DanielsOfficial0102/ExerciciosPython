#Atividade 06 - Lógica de Programação
#2. Escreva um programa que mostre as tabuadas dos números de 1 a 10, ou seja, toda a Tabuada.


x = 1

y = 1

while (y < 11):

    print ('Tabuada:',y)
    print('\n')

    while (x < 11):        

        print('{} x {:2} = {}'.format(y, x, y * x))

        x += 1

    y += 1

    x = 1


    print ('\n')

    print ('========================')

    print ('\n')


input('Pressione Enter Para Sair')
           

