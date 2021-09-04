#Atividade 05 - Lógica de Programação

#2. Escreva um programa que permita a entrada de dados para o cálculo de índice de massa corporal (IMC) em que sejam exibidas as classificações
#(Exemplo: Magro, Saudável, Gordo, etc...) para cada resultado obtido a partir desse cálculo.


'''Qual é a MASSA CORPORAL'''

p = float(input('Qual é seu peso? (kg) '))

a = float(input('Qual é a sua altura? (Mts) '))

imc = p / (a * a)

if (imc <= 0) and (imc <= 17):
    print('Magreza grave')

elif (imc <= 18):
    print('Abaixo do peso')

elif (imc <= 24):
    print('Peso normal')

elif (imc <= 29):
    print('Acima do peso')

elif (imc <= 34):
    print('Obesidade 1')

elif (imc <= 39):
    print('Obesidade 2')

else:
    print('Obesidade 3')

print(imc)
input("Pressione Enter para sair...")
