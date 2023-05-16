#2 listas una con nombres otra con apellidos
nombres = ["Wilmer","Carlos","Mario","Catalina","Roberto"]
apellidos = ["Perez","Correa","Almeida","Zapata","Osorio"]

#registrar esta infomacion en un TXT de forma optima
with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son: \n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------------\n") for n,a in zip(nombres,apellidos)]