#Atividade 06 - Lógica de Programação
#6. Faça um programa que permita a entrada dos valores do Etanol e da Gasolina e permita descobrir para cada inserção qual dos combustíveis era o mais viável.
#Ao final, informe quantas vezes tanto o Etanol, quanto a Gasolina foi o combustível mais viável.
#Você pode determinar quantas serão as entradas para Etanol e Gasolina, ou seja, se serão entradas por 10 ou 30 vezes, etc.

contgasolina = 0

contetanol = 0

for i in range (0, 10, 1):

    print('\n')
    
    gasolina = float(input('Qual o valor da GASOLINA: R$ '))

    print('\n')

    etanol = float(input('Qual o valor do ETANOL: R$ '))

    print('\n')
    
    if(etanol < (gasolina * 0.7)):
        print('ETANOL é mais viavel!!!!')
        contetanol = contetanol + 1

    else:
        print('GASOLINA é mais viavel!!!!')
        contgasolina = contgasolina + 1

    print('\n')

    print('=========================================')

    print('\n')

print('Quantidade de vezes em que o ETANOL foi mais viavel: ', contetanol)
print('Quantidade de vezes em que a GASOLINA foi mais viavel: ', contgasolina)


input('Pressione Enter Para Sair')
    
    
