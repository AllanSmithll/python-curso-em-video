# 11/10/2022
# Vários valores numéricos e cadastrar em uma lista. Caso o número já exista, ele não será adicionado. No final, mostrar todos os números diferentes, e em ordem crescente

numeros = list()
escolha = "S"
while escolha == 'S':  # Continue enquanto o usuário escolher "SIM"
    numeros.append(float(input('Digite um número: '))) # Solicite
    escolha = input('Vai escolher algum número (s ou n)? ').upper() # Vai escolher mais um número?
    if escolha == "S":
        continue   # Se sim, continue solicitando
    elif escolha == 'N': 
        break      # Se não, pare de solicitar
print(numeros)

