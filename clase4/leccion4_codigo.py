import pdb 
pdb.set_trace()

#ejercicio 1
mi_lista = [[1,2,3],[12,15,18,100,435,76],[534,876,809,1,56,878,90]]
nueva_lista = [max(i) for i in mi_lista]
print(nueva_lista)

#ejercicio 2
lista2 = [3, 4, 8, 5, 5, 22, 13, 24, 45, 31, 179]

def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

primos = list(filter(es_primo, lista2))

print(primos)


