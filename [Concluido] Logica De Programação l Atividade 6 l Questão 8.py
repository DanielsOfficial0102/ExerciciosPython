#Atividade 06 - Logica De Programação
#8. Escreva um programa de computador que permita a entrada de 10 números e, ao final, mostre qual foi o menor numero digitado da sequencia

menor = float("inf")


for num in range(0,11):
    num = int(input('Digite um numero : '))

    if num < menor:
        menor = num

print('O menor numero é : ', menor)

input('Tecle Enter')
    
    
