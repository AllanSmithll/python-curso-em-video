# 12/01/2023, aula de exceções (a última aula do Mundo 3 de Python)

try: # Tente fazer esta operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro: # Caso dê algum erro, lance uma exceção
    print(f'Encontramos um problema na digitação: {erro}. :(')
else: # Se deu tudo certo, printe isso
    print(f'O resultado foi {r}.')
finally: # Mesmo dando certo ou errado, printe isso de qualquer forma
    print('Volte sempre!')