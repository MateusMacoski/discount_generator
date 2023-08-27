# Bem-vindo
print('Bem-vindo a loja do Mateus Macoski')

# Valor da unidae e quantidade do produto
valor_unid = float(input('Digite o valor unitário do produto: '))
total_unid = int(input('Digite a quantidade do produto: '))

# subtotal valor total sem desconto
subtotal_sem_desconto = valor_unid * total_unid

# desconto com base na quantidade
if total_unid < 200:
    desconto = 0
elif total_unid >= 200 and total_unid < 1000:
    desconto = 0.05
elif total_unid >= 1000 and total_unid < 2000:
    desconto = 0.10
else:
    desconto = 0.15

# Valor total com desconto
total_com_desconto = subtotal_sem_desconto * (1 - desconto)

# Resultados
print('Resumo do Pedido:')
print('Valor Unitário: R${:.2f}'.format(valor_unid))
print('Quantidade: {}'.format(total_unid))
print('Valor Total (sem desconto): R${:.2f}'.format(subtotal_sem_desconto))
print('Desconto aplicado: {:.0%}'.format(desconto))
print('Valor Total (com desconto): R${:.2f}'.format(total_com_desconto))