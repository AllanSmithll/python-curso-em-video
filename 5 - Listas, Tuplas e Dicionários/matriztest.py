nlin = 3
ncol = 3
m = [[2] * ncol for i in range(nlin)]
for i in range(nlin):
    for j in range(ncol):
        print(f'{m[i][j]:4}',end='')
    print()