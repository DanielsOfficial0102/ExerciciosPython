#Atividade 02 - Lógica de Programação

#4. É necessário saber o índice corporal de massa (IMC) de uma pessoa. Para tal, faça um programa de computador que efetue esse cálculo em que é necessário mostrar o resultado para esse cálculo.Exiba o resultado na tela. *

'''Qual é a MASSA CORPORAL'''

p = float(input('Qual é seu peso? (Kg): '))
a = float(input('Qual é a sua altura? (Mts): '))
imc = p / (a ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
input('Para sair aperte ENTER')
