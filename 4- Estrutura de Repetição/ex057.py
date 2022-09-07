sexo = input('Qual seu sexo (M/F): ').upper().strip()[0]
while sexo not in "MmFf":
    sexo = input('Sexo inválido. Digite o sexo novamente: ').strip().upper()[0]
print('OK! Sexo validado com sucesso.')