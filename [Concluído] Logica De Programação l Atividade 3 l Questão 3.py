#Atividade 03 - Lógica de Programação

#3. Com base nas informações acima.
#faça um programa que permita a entrada do valor da gravidade e o tempo de duração da queda e retorne a VELOCIDADE dessa queda.


"Qual é a velocidade"


g = int(input('Qual é o valor da GRAVIDADE? : '))

t = int(input('Qual é o TEMPO de duração de QUEDA? : '))

velocidade = g * (t ** 2) / 2

print('A velocidade é de: {:.0f} M/s² :'.format(velocidade))

input('Precione a Tecla Enter Para Sair')
