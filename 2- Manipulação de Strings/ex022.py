nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome completo em maiúsculas será {}.'.format(nome.upper()))
print('Seu nome completo em minúsculas será {}.'.format(nome.lower()))
print('A quantidade total de letras do seu nome completo é {} letras.'.format(len(nome) - nome.count(' ')))
#print('O seu nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
print(' ')
print('Feito em 23/02/2022.')
