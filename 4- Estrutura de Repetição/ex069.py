escolha = 'S'
while escolha == 'S':
    #Variáveis de contagem
    cont_p_maior = 0   #Quantas pessoas tem mais de 18 anos
    cont_m = 0   #Quantos homens fizeram a pesquisa
    cont_f_jovem = 0   #Quantas mulheres jovens fizeram a pesquisa

    #Coleta de dados
    idade = int(input('Quantos anos você tem? '))
    sexo = input('Sexo (M/F): ').upper
    if idade >= 18:
        cont_p_maior += 1
    if sexo == 'M':
        cont_m += 1
    if sexo == 'F' and idade >= 20:
        cont_f_jovem += 1

    escolha = input("Quer continuar a pesquisa (s/n)? ").upper()
    if escolha == 'S':
        continue
    elif escolha == "N":
        break

print(f'Pessoas com mais de 18 anos: {cont_p_maior}.')
print(f'Homens cadastrados: {cont_m}.')
print(f'Mulheres com menos de 20 anos: {cont_f_jovem}.')