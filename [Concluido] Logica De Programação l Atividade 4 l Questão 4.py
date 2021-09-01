#ATIVIDADE 04 - LÓGICA DE PROGRAMAÇÃO

#4. Faça um programa que permita o cálculo da velocidade média, conforme a fórmula na imagem.
#Sabendo que a via aceita a velocidade de 100 Km/h, informe se o indivíduo foi multado ou está dentro do limite de velocidade. *


"Radares De Rodovia"

k = float(input('Qual a quilometragem percorrida pelo motorista ?, Quilometros : '))
t = float(input('Qual foi o tempo que ele levou para chegar ?, Minutos : '))

velocidade = (k / t) * 60

print('A velocidade média é : ', velocidade)

if(velocidade>100):
    print('Você foi multado ! ! ! Exedeu o limite permitido de 100 KM/H')

else:
    print('Parabens Você dirige muito bem ! ! !')

input('Precione Enter Para Sair')


#Concluido
