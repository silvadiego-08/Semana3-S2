#Cálculo del tiempo total de un viaje con escalas
input("Bienvenido a tu calculadora de tiempo de viaje con escalas. Presiona Enter para continuar.")
#Solicitar la primera duracion del tramo de vuelo
duracion1 = int(input("Introduce la duración del primer tramo de vuelo en horas: "))
#Ingresar la duración de la primera escala. 
escala1 =int(input("Introduce la duración de la primera escala en horas: "))
#Solicitar la segunda duracion del tramo de vuelo
duracion2 = int(input("Introduce la duración del primer tramo de vuelo en horas: "))
#Ingresar la duración de la segunda escala.
escala2 =int(input("Introduce la duración de la segunda escala en horas: "))
#Solicitar la tercera duracion del tramo de vuelo
duracion3 = int(input("Introduce la duración del primer tramo de vuelo en horas: "))
#Sumar la duración del primer tramo con la primera escala. 
tiempo1 = duracion1 + escala1
#Sumar el resultado con el segundo tramo del vuelo.
tiempo2 = tiempo1 + duracion2
#Sumar el resultado con la segunda escala.
tiempo3 = tiempo2 + escala2
#Sumar el resultado con el tercer tramo del vuelo.
tiempo_total = tiempo3 + duracion3
#Mostrar el tiempo total del viaje.
print(f"El tiempo total del viaje es: {tiempo_total} horas")
#Fin del programa