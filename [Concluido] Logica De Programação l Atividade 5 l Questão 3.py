#Atividade 05 - Lógica de Programação

#3. Faça um programa que permita a entrada de uma idade de um indivíduo e exiba a classificação etária de acordo com as faixas de valores a seguir.


print(' Criança de 0 Até 11 Anos ')
print(' Adolescente De 12 Até 18 Anos ')
print(' Jovem De 19 Até 24 Anos ')
print(' Adulto De 25 Até 40 Anos ')
print(' Meia Idade Para 41 até 60 anos ')
print(' Idoso Acima De 60 Anos \n\n' )


x = int(input('Digite sua idade: '))

if (x>=0) and (x<=11): 
    print('Você è uma Criança')

elif (x<18):
    print('Você é um Adolescente')


elif (x<24):
    print('Você é Jovem')

elif (x<40):
    print('Você é Adulto')

elif (x<60):
    print('Você esta na Meia Idade')

else:
    print('Você é Idoso')

input('Tecle Enter Para Sair')    
