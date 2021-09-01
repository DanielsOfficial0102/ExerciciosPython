#Atividade 03 - Lógica de Programação

#4. Com base nas informações acima, faça um programa que permita a entrada do valor da gravidade e o tempo de duração da queda,
#que permita descobrir de que ALTURA o objeto caiu.

#Calcular a altura que um objeto caiu

g = float(input('Qual o valor da força gravitacional? : '))
t = float(input('Qual Foi o Tempo Da Velocidade De Queda? : '))

D = g*(t**2)/2

print('A altura que o objeto caiu é de: ', D, 'm')

input('Pressione Enter para sair…')
