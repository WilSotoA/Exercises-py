import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\visitas.csv")

#creando el grafico
sns.lineplot(x="fecha",y="veces",data=df)

#creando un punto en el mayor numero de visitas
plt.plot("01-11",34,"o")

#mostrando el grafico
plt.show()