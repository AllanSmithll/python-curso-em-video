s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i #s = s + 1
print(f'A soma de todos os valores solicitados é {s}.')