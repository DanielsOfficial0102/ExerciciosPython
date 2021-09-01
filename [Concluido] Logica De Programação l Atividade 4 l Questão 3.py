#ATIVIDADE 04 - LÓGICA DE PROGRAMAÇÃO

#3. Escreva um programa que permita a entrada de dados para o cálculo de índice de massa corporal (IMC) em que sejam exibidas as duas classificações
#(Exemplo: "Peso ideal" e "Acima do peso") para cada resultado obtido a partir desse cálculo. Veja hiperlink a seguir que mostra essa tabela…

#Índice corporal

'''Qual é a MASSA CORPORAL'''

p = float(input('Qual é seu peso? (kg) '))

a = float(input('Qual é a sua altura? (Mts) '))

imc = p / (a ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
      
if(imc <= 24.9):
      
 print('Abaixo do peso')
else:
 print('acima do peso')

input("Pressione Enter para sair...")

