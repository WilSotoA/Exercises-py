#si el modulo estuviera dentro de una carpeta en la misma ruta
#import funciones_2.0.saludar as m_saludar

#agregar un modulo que esta fuera de la carpeta
import sys
sys.path.append("d:\\BLAZE\\Documents\\Wilmer\\Projectos Wil\\Exercises py\\funciones_2.0")
import saludar as modulo_saludar

print(modulo_saludar.saludar("Dalto"))