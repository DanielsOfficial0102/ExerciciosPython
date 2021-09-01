#Atividade 02 - Lógica de Programação

#3. Faça um programa de computador em que se permita a entrada de uma temperatura em Fahrenheit e converta para graus Célsius, mostrando em seguida o resultado da conversão. Faça uma pesquisa na Internet para descobrir a fórmula de conversão.

f = float(input('Informe a temperatura em ºf : '))

c = ((5 * f) / 9)

print('A temperatura de {} ºf corresponde a {:.1f}ºc!'.format(f, c))

input('Para sair aperte ENTER')
