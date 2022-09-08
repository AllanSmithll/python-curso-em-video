#Campeonato Brasileiro no dia 07/09/2022
brasileirao = ('PALMEIRAS', 'FLAMENGO', 'CORINTHIANS', 'INTERNACIONAL', 'FLUMINENSE', 'ATHLÉTICO-PR', 'ATLÉTICO-MG', 'AMÉRICA-MG', 'GOIÁS', 'SANTOS', 'BRAGANTINO', 'FORTALEZA', 'BOTAFOGO', 'SÃO PAULO', 'CEARÁ', 'CUIABÁ', 'CORITIBA', 'AVAÍ', 'ATLÉTICO-GO', 'JUVENTUDE')

brasa_primeiros = ['']
for i in brasileirao: #Os 6 primeiros colocados
    if i == 0:
        brasa_primeiros.append(brasileirao[i])
    elif i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
        brasa_primeiros.append(brasileirao[i])
    else:
        pass
print(brasa_primeiros)
