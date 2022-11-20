# 1- Função soma
#Aula de Funções
def soma(a, b):
    s = a + b
    print(f'A + B = {s}')

#Programa principal
soma = (2, 4)
print('Olá')


# 2- Função quando temos mais de um parâmetro
def contador(* num):
    tam = len(num)
    print(f'A tupla tem os valores {num}, contendo {tam} números.')


contador(1, 2, 3)
contador(2, 4, 6, 8)
contador(2, 3, 5, 7, 11)

# 3- Usando lista
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [2, 3, 4, 5, 6]
dobra(valores)
print(valores)

# 4- Desempacotamento
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}.')

soma(5, 2)
soma(19, 23, 40)

