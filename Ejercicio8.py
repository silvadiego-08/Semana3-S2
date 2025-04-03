# Conversión de una cantidad en dólares a distintas monedas (euros, libras y yenes)
dolares = float(input("Introduce la cantidad en dólares: "))
#Tipo de cambio a euros, libras y yenes.
euros = dolares * 0.85
libras = dolares * 0.75
yenes = dolares * 110.0
#Mostrar el resultado en euros, libras y yenes.
print(f"{dolares} dólares son {euros:.2f} euros, {libras:.2f} libras y {yenes:.2f} yenes.")
