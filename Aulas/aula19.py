# 20/10/2022

# Estrutura básica

print ('''-=-=-=-=-=-=-=-=-=-=-=-=-= Exemplo 1 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
dados = dict() # Estrutura com valores e chaves
dados = {
    'nome': "Allan",
    'idade': 18,
    'sexo': 'M'
}

print(dados)
print(dados['nome']) # Printar apenas uma das propriedades com seu valor
print(dados['idade'])
print(dados['sexo'])
del dados['sexo']  # Deletar uma propriedade/chave
print(dados)

print('''\n-=-=-=-=-=-=-=-=-=-=-=-=-=-= Exemplo 2 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme.values())  # Quando quero apenas os valores. Por exemplo: Stars Wars, 1977 e George Lucas.
print(filme.keys())  # Quando quero apenas as keys. Por exemplo: titulo, ano e diretor.
print(filme.items())  # Quando quero todos os items. Todos os valores com suas keys.

for key, value in filme.items():
    print(f'\n O {key} é {value}.')
