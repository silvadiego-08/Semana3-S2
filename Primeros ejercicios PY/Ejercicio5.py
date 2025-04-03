#Conversión de unidades de tiempo 
segundos = int(input("Introduce el tiempo en segundos: "))
#Dividir los segundos entre 3600 para obtener las horas. 
horas = segundos / 3600
#Guardar la parte entera del resultado como horas. 
horas = int(horas)
#Multiplicar las horas obtenidas por 3600
minutos = (horas * 3600) / 60
minutos = int(minutos)
#Multiplicar los minutos obtenidos por 60.
segundos = (minutos * 60) / 60
#Mostrar el resultado en horas, minutos y segundos.
print(f"{horas} horas, {minutos} minutos y {segundos} segundos")

