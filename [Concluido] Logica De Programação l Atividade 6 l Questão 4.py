#Atividade 06 - Lógica De Programação
#4. Gere um programa que some todos numeros que foram inseridos pelo usuario e exiba o somatorio destes numeros
#usuário pode inserir ate 10 numeros reais.

soma = 0
cont = 0
for c in range(1, 11):
    num = int(input('Digite um número : '))
    soma += num
    cont += 1
print('Você informou {} números e a soma foi {}'.format(cont, soma))


input('Pressione a Tecla Enter')

