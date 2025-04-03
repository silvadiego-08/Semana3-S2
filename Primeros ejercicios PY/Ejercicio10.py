#Cálculo del volumen de un cilindro y su área superficial 
radio_cilindro = float(input("Introduce el radio del cilindro: "))
altura_cilindro = float(input("Introduce la altura del cilindro: "))
#Calcular el área de la base multiplicando PI por el radio al cuadrado.
area_base = 3.14159 * (radio_cilindro ** 2)
volumen_cilindro = area_base * altura_cilindro
#Calcular el area lateral
area_lateral = 2 * 3.14159 * radio_cilindro * altura_cilindro
area_superficial = area_lateral + (2 * area_base)
input("radio_cilindro, altura_cilindro")
input("El volumen calculado es: ", volumen_cilindro)
input("El área superficial calculada es: ", area_superficial)
