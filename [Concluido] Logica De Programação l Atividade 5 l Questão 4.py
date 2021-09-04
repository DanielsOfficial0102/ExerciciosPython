
import durante
from saida02 import saida

vh = float(input('\nDigite o valor das horas trabalhadas: R$ '))

ht = float(input('\nDigite as horas trabalhadas: HrS '))
print('\n====================================================')

sal_bruto = vh * ht

process(irpf)
process(inss)
process(cm)
process(vt)
process(vr)
process(co)
process(descontos)

print('\nO valor de sal_bruto é : R$  ',sal_bruto)
print('\n====================================================')


sal_bruto = sal_bruto - descontos

saida(resp)
input('\nDigite ENTER para Sair...')
