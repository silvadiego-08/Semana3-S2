#Calculo del indice de masa corporlal (IMC)
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
#Calcular el IMC
IMC = peso / (altura ** 2)
#Mostrar el resultado del IMC
#Clasificar el IMC
print(f"Tu IMC es: {IMC:.2f}")
print("Clasificación del IMC:")
print(peso, altura)
if IMC < 18.5:
    print("Bajo peso")
elif 18.5 <= IMC < 24.9:
    print("Peso normal")

