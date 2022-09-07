salário = float(input('Qual o salário anterior? R$'))
novo = salário + (salário * 15 / 100)
print('Antes, o salário era R${:.2f}. Após o aumento de 15%, passou a receber R${:.2f}.'.format(salário, novo))
print('Concluído em 29/12/2021, para ser um aumento salário de 15%.')
