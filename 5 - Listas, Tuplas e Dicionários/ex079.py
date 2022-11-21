# 11/10/2022
# Vários valores numéricos e cadastrar em uma lista. Caso o número já exista, ele não será adicionado. No final, mostrar todos os números diferentes, e em ordem crescente

numeros = list()
escolha = "S"
while escolha == 'S':  # Continue enquanto o usuário escolher "SIM"
    num = float(input("Digite um número: "))
    for i in numeros:
        if num in numeros:
            print("Por favor, digite outro número. Tem que ser um que não exista na lista!\n")
            num = float(input("Digite novamente: "))
            if num not in numeros:
                break
            else: 
                continue
    numeros.append(num) # Solicita
    escolha = input('Vai escolher algum número (s ou n)? ').upper() # Vai escolher mais um número?
    
    if escolha == "S":
        continue   # Se sim, continue solicitando
    elif escolha == 'N': 
        break      # Se não, pare de solicitar

numeros.sort()
print(numeros)

