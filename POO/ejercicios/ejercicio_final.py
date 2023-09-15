from textblob import TextBlob


class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        elif analisis.sentiment.polarity == 0:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"


analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("Hi, how are you")
print(resultado)

# openai

# import openai

# openai.api_base = "http://openai.com"

# system_rol = """seras un analizador de sentimientos el cual recibe
#                 un mensaje y dependiendo del mismo devuelves un int o
#                 un float"""

# mensajes = [{"role": "system", "content": system_rol}]


# class Sentimiento:
#     def __init__(self, nombre, color) -> None:
#         self.nombre = nombre
#         self.color = color

#     def __str__(self):
#         return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)


# class AnalizadorDeSentimientos:
#     def __init__(self, rangos) -> None:
#         self.rangos = rangos

#     def analizar_sentimiento(self, polaridad):
#         for rango, sentimiento in self.rangos:
#             if rango[0] < polaridad <= rango[1]:
#                 return sentimiento
#         return Sentimiento("Muy negativo", "31")


# rangos = [
#     ((-0.6, -0.3), Sentimiento("Negativo", "31")),
#     ((-0.3, -0.1), Sentimiento("algo negativo", "31")),
#     ((-0.1, 0.1), Sentimiento("Neutral", "33")),
#     ((0.1, 0.4), Sentimiento("Algo positivo", "32")),
#     ((0.4, 0.9), Sentimiento("Positivo", "32")),
#     ((0.9, 1), Sentimiento("Muy positivo", "32")),
# ]


# analizador = AnalizadorDeSentimientos(rangos)
# resultado = analizador.analizar_sentimiento(0.9)
# print(resultado)

# while True:
#     user_prompt = input("\x1b[1;32m" + "\nPuedes escribir algo" + "\x1b[0;37m")
#     mensajes.append({"role": "user", "content": user_prompt})

#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo", messages=mensajes, max_tokens=8
#     )

#     respuesta = completion.choices[0].message["content"]

#     mensajes.append({"role": "assistant", "content": respuesta})

#     sentimiento = analizador.analizar_sentimiento(float(respuesta))
#     print(sentimiento)
