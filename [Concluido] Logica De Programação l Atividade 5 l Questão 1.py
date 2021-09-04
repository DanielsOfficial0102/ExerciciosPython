#Atividade 05 - Lógica de Programação

#1. Escreva um programa de computador em linguagem Python em que sejam permitidas a entrada de 3 notas (números reais),
#que faça o cálculo da média dos alunos e, conforme a nota obtida na média seja exibida uma das mensagens, conforme a classificação abaixo:

#Nota até 1,99 - Péssimo
#Nota até 3,99 - Ruim
#Nota até 5,99 - Regular
#Nota até 7,99 - Bom
#Nota até 9,5 - Ótimo
#Nota até 10 - Excelente


media = 0.0

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3)//3

print('O valor da média final é: ', media)

if(media < 2):
    print('Péssimo')

elif(media < 4):
    print('Ruim')

elif(media < 6):
    print('Regular')

elif(media < 8):
    print('Bom')

elif(media < 10):
    print('Ótimo')

elif(media == 10):
    print('Excelente')

input('Pressione a Tecla Enter')    
