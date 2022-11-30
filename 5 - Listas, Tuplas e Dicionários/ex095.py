# 26/11/2022
'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

# jogadores = dict() # Crio um dicionário

# escolha = 'NÃO'
# while escolha != 'SIM':
#     jogadores = [{
#         "id": 1,
#         "nome": input("Nome: "),       # Pergunto o nome do jogador
#         "partidas_jogadas": int(input("Partidas Jogadas: "))       # Quantas partidas foram jogadas pelo tal jogador
#     },
#     ]

#     MAX_PARTIDAS = 38         # Máximo de partidas do campeonato
#     if jogadores["partidas_jogadas"] < MAX_PARTIDAS:          # Se o jogador joga menos de 38 partidas do campeonato
#         MAX_PARTIDAS = int(jogadores["partidas_jogadas"])         # Então a média só terá as partidas jogadas pelo jogador
#     elif jogadores["partidas_jogadas"] > MAX_PARTIDAS: 
#         raise Exception(f"Número de partidas jogadas superior a {MAX_PARTIDAS}. Digite novamente.")            # Ele simplemente não pode jogar mais do que o máximo de partidas do campeonato

#     gols_totais = 0
#     for i in range(MAX_PARTIDAS):
#         gols_partida = int(input(f"Quantos gols na partida {i+1}? "))      # Gols na partida
#         gols_totais += gols_partida            # Somar os gols totais

#     media_gols_totais = gols_totais / MAX_PARTIDAS           # Média de gols no campeonato

#     jogadores["total_gols"] = gols_totais              # Adicionar o atributo "total_gols" com o valor "gols_totais", que é o total de gols feitos pelo jogador
#     jogadores["gols_media"] = media_gols_totais            # Média de gols totais

#     escolha = jogadores.append(input(""))


# print(jogadores) # Para vermos o resultado
