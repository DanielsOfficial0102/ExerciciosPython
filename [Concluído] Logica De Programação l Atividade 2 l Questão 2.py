#Atividade 02 - Lógica de Programação

#3. Faça um programa de computador em que se permita a entrada de uma temperatura em Fahrenheit e converta para graus Célsius, mostrando em seguida o resultado da conversão. Faça uma pesquisa na Internet para descobrir a fórmula de conversão.

'''Permita que o usuário entre com os valores'''

b = float(input('Qual é o valor da base? '))
a = float(input('Qual é o valor da altura? '))
t = (b*a)/2
print('O valor da area entre {} e {} é {}'.format(b,a,t))
input('Aperete ENTER pra sair')
