#Atividade 03 - Lógica de Programação

#1. Escreva um programa que permita o cálculo da velocidade média de um veículo conforme as entradas de dados necessários.
#Para isso, leia o texto abaixo

#Como calcular a velocidade de um carro? --> Por exemplo,
#vamos supor que um carro dirigido por uma pessoa gastou 3 horas para percorrer 240 quilômetros.
#A velocidade média será determinada através da divisão entre a distância e o tempo gasto na viagem.
#Veja: Nessa viagem, o carro desenvolveu uma velocidade média de 80 km/h.

#D = Distancia
#V = Velocidade
#T = Tempo

d = float(input('Insira a Distancia Percorrida : ' ))
t = float(input('Insira o Tempo Percorrido : ' ))
velocidade = d/t
print('O Tempo Gasto Total Dessa Viagem Foi De : ', velocidade)
