#Atividade 06 - Lógica de Programação
#3. Faça um programa que exiba todos os números ímpares dentre a faixa de 0 a 50
#separados por hífen (por exemplo: " 3 - 5 - 7 - ...")

cont = 1

while (cont < 50):
    print(cont, end= ' - ')
    cont = cont + 2

else:
    print('\n Finalizado Com Sucesso ! ')


input('Pressione Enter Para Sair')
