n=[6,4,3,5,2,1]
aux = 0;

tam = len(n)

for i in range(0,tam):

    for j in range(0,tam-1):

        if(n[j] > n[j+1]):
            aux = n[j]
            n[j] = n[j+1]
            n[j+1] = aux

print(n)