#Atividade 03 - Lógica de Programação

#2. Faça um programa que calcule a distância percorrida por um veículo.

#Qual é a fórmula para calcular a distância? ---> Para fazer esse cálculo você deve usar a seguinte fórmula: d= v x t (Distância é igual à velocidade vezes o tempo).
#Por exemplo, caso o indivíduo deseje calcular a distância percorrida pelo o seu carro,
#primeiramente ele deve saber a velocidade média do carro e o tempo de viagem.6

#Velocidade Media

v = float(input('Qual a Velocidade Percorrida ? : '))
t = float(input('Qual o Tempo Percorrido ? : '))
d = v * t

print('Á Distancia Percorrida Foi : ', d)
