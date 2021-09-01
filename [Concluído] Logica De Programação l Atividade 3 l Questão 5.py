#Atividade 03 - Lógica de Programação

#5. Com base nas informações acima, faça um programa que permita a entrada da velocidade,
#bem como o valor da gravidade e retorne o TEMPO decorrido da determinada queda.
#Necessária pesquisa da fórmula.

g = float(input('Digite o valor da gravidade ? : '))
t = float(input('Digite qual a velocidade ? : '))
te = (t / g)
print('O tempo de queda é  {:.1f} '.format(te))

input('Precione a Tecla Enter Para Sair')
