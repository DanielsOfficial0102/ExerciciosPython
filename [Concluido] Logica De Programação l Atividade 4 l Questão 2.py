#ATIVIDADE 04 - LÓGICA DE PROGRAMAÇÃO

#2. Escreva um programa em linguagem Python em que sejam permitidas a entrada de 3 notas (números reais), que faça o cálculo da média dos alunos
#exibindo a mensagem de "Aluno aprovado!" para notas iguais ou superiores a 6 e a mensagem de "Aluno Reprovado!" para as demais notas.


#Cálculo da média simples de 3 notas

media = 0.0

nota1 = float(input('Digite a primeira nota : '))
nota2 = float(input('Digite a segunda nota : '))
nota3 = float(input('Digite a terceira nota : '))

media = (nota1 + nota2 + nota3)/3

print("O valor da média final é : ", media)

if( media >= 6):
    print("O Aluno foi APROVADO...")

else:
    print ("O Aluno foi REPROVADO...")
      

input('Pressione Enter para sair...')

