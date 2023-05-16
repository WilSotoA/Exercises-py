import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo lo datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordenando el dataframe por la edad descendente
df_orden_descendente = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primer fila con head()
primer_fila = df.head(1)

#accediendo a la ultima fila con head()
ultima_fila = df.tail(1)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe:
df_info = df.describe()

#accediendo a la edad de la fila 1
elemento_especifico_loc = df.loc[1,"edad"]

#accediendo a la edad de la fila 1 con iloc
elemento_especifico_iloc = df.iloc[1,2]

#accediendo a todas las filas de una columna
apellidos = df.iloc[1,:]

#accediendo a filas con edad mayor que 18
mayor_que_30 = df.loc[df["edad"]>18,:]

print(mayor_que_30)