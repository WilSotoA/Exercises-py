def sumar_dos():
    while True: 
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b)
        except Exception as e:
            print("Por favor  ingrese SOLO numeros")
            print(f"ERROR {e}")
        else:
            break
        finally:
            print("Manejo de excepcion finalizado")
    return resultado
print(sumar_dos())