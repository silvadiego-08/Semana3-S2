temp_fah = float(input("Ingrese la temperatura en Fahrenheit: "))
temp_cel = ((temp_fah - 32) * 5) / 9
temp_kel = temp_cel + 273.15

# Mostrar resultados
print(f"Grados celsius: {temp_cel:.2f}")
print(f"Grados kelvin: {temp_kel:.2f}")
print(f"Grados fahrenheit: {temp_fah:.2f}")