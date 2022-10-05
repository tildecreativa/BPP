from math import sqrt


#print('Escribe un número')

def resta(x):
    #print(x-(x-1))
    return x-(x-1)

def suma(x):
    #print(x+(x+1))
    return x+(x+1)

def menorque100(x):
    if(x<100):
        #print('menor que 100')
        return True
    else:
        #print('mayor o igual a 100')
        return False

def numeroprimo(x):
    n = x
    prime_flag = 0
    
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            #print("Primo")
            return True
        else:
            #print("No es primo")
            return False
    else:
        #print("No es primo")
        return False

def parimpar(x):
    if x & 1 == 0:
        #print("Es par")
        return 'par'
    else:
        #print("Es impar")
        return 'impar'


'''try:
    x = int(input())
except:
    print('no es un número')
else:
    resta(x)
    suma(x)
    numeroprimo(x)
    parimpar(x)'''