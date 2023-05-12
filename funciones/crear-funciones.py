#creando una función simple
def saludar():
    print("Hola Wilmer, como estas")
#ejecutando la funcion simple
saludar()

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "dama"
    elif sexo == "hombre":
        adjetivo = "caballero"
    else:
        adjetivo = "ente"
    print(f"Hola {nombre}, como esta {adjetivo}?")
    
saludar("Albeiro","binario")

#crear una funcion que retorna multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3= num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num_entero*2}"
    return contraseña,num
    
#desempaquetando valores retornados por funcion
password,primer_numero = crear_contraseña_random(3)
print(f"Tu contraseña nueva es: {password}")

print(f"El numero para crearla fue: {primer_numero}")