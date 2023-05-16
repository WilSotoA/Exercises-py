import re
texto = "Hola Andres, mi numero es +57 321 928 2112"

pattern = r"\+\d{2}\s\d{3}\s\d{3}\s\d{4}"

reemplazo = re.sub(pattern,"(numero oculto)",texto)

print(reemplazo)