# creando una funcion que nos devuelva los numeros primos

#crear una funcion que verifique si un numeros es primo
def es_primo(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True

#creando una funcion que retorne una lista con todos los primos
def primos_hasta(num):
    primos = []
    for i in range(3,num + 1):
        resultado = es_primo(i)
        if resultado == True:
            primos.append(i)
    return primos


resultado = primos_hasta(98)
print(resultado)
