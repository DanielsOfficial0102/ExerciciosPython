#Atividade 06 - Lógica de Programação
#7. Faça uma programa que permita a geração de até 10 bilhetes aleatórios da loteria,
#porém a exibição destes do modelo para estes bilhetes deve ser próxima da imagem anexa (NÃO NECESSARIAMENTE IGUAL, MAS PRÓXIMA).
#abaixo a linhas de comandos que permitem gerar uma linha apenas de números aleatórios. *

import random

input("Pressione ENTER pra gerar os números: ")

while True:
       
          num1 = random.sample(range(0,61),6)
          num2 = random.sample(range(0,61),6)
          num3 = random.sample(range(0,61),6)
          num4 = random.sample(range(0,61),6)
          num5 = random.sample(range(0,61),6)
          num6 = random.sample(range(0,61),6)
          num7 = random.sample(range(0,61),6)
          num8 = random.sample(range(0,61),6)
          num9 = random.sample(range(0,61),6)
          num10 = random.sample(range(0,61),6)
         

          if num1 not in (num2,num3,num4,num5,num6)and num2 not in (num3,num4,num5,num6)and num3 not in (num4,num5,num6)and num4 not in (num5,num6)and num5 != num6:
              break
          
    
print('Os números são:\n', num1,num2,num3,num4,num5,num6,num7,num8,num9,num10)

input('Pressione Enter Para Sair')


