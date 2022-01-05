n=[4,5,2,7,1,6,8,3]

aux=0
tam = len(n)
for i in range(0,tam):

    for j in range(0, tam-1):
        if (n[j] > n[j+1]):
            aux = n[j]
            n[j] = n[j+1]
            n[j+1] = aux
print("Ordered via bubble sort: ")
print(n)
