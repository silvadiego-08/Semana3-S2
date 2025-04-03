#Cálculo del tiempo total de una película con comerciales 
duracion_pelicula = int(input("Introduce la duración de la película en minutos: "))
comerciales_previos = int(input("Introduce la duración de los comerciales previos en minutos: "))
pausas_comerciales_cant = int(input("Introduce la cantidad de pausas comerciales: "))
pausas_comerciales_dur = int(input("Introduce la duración de cada pausa comercial en minutos: "))
#Multiplicar la cantidad de pausas comerciales por la duración de cada pausa.
total_comerciales = pausas_comerciales_cant * pausas_comerciales_dur
#Sumar la duración de la película con los comerciales previos.
duracion_total = duracion_pelicula + comerciales_previos
#Sumar el resultado con el total de comerciales.
duracion_total = total_comerciales + duracion_total
#Mostrar la duracion original de la pelicula
print(f"La duración total de la película es: {duracion_total} minutos")
print(f"La duracion de los comerciales totales es: {total_comerciales} minutos")
#Mostrar el tiempo total de proyeccion
duracion_pelicula = duracion_pelicula + comerciales_previos + total_comerciales
print(f"La duración total de proyección es: {duracion_pelicula} minutos")
