#promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duración
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#Mostrando las difrencias de duración (ejercicio A)
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento")
print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el mas promedio")

#mostrando la cantidad de espacios vacios que se reducen (ejercicio B)
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"El curso de dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio")

#mostrando diferencias si los cursos duraran 10 horas 
print(f"ver 10 de horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"ver 10 de horas de este curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de otros cursos")
