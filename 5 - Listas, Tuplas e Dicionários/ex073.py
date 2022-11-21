#Campeonato Brasileiro no dia 07/09/2022
brasileirao = ('PALMEIRAS', 'FLAMENGO', 'CORINTHIANS', 'INTERNACIONAL', 'FLUMINENSE', 'ATHLÉTICO-PR', 'ATLÉTICO-MG', 'AMÉRICA-MG', 'GOIÁS', 'SANTOS', 'BRAGANTINO', 'FORTALEZA', 'BOTAFOGO', 'SÃO PAULO', 'CEARÁ', 'CUIABÁ', 'CORITIBA', 'AVAÍ', 'ATLÉTICO-GO', 'JUVENTUDE')
print(f'Lista de times: {brasileirao}')

print(f"\nOs 6 primeiros times são: {brasileirao[0:6]}")
print(f"Os 4 últimos times são: {brasileirao[16:21]}")
print(f"Times em ordem alfabética: {sorted(brasileirao)}")
print(f"Corinthians: {brasileirao.index('CORINTHIANS')+1}ª posição.")
