#Atividade 06 - Lógica de Programação
#5. Crie um programa de computador que some apenas os números ímpares inseridos pelo usuário e mostre o resultado desta soma ao final.
#O usuário pode inserir 10 números inteiros.

soma = 0
cont = 0
for c in range(1, 11):
    num = int(input('Digite um número : '))
    if num % 2 == 1:
        soma += num
        cont += 1
print('Você informou {} números ínpares e a soma foi {}'.format(cont, soma))


input('Pressione a Tecla Enter')


