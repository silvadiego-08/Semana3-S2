#Calculo de salario neto
salario = int(input("Introduce el salario bruto: "))
#Calcular el 10% del salario como impuesto sobre la renta
impuesto = salario * 0.10
#Calcular el 5% del salario como seguro social
seguro_social = salario * 0.05
#Calcular el 3% del salario como fondo de pensiones. 
fondo_pensiones = salario * 0.03
#Sumar todos los descuentos calculados. 
descuentos = impuesto + seguro_social + fondo_pensiones
#Restar los descuentos al salario bruto. 
salario_neto = salario - descuentos
#Mostrar el salario bruto. 
print(f"El salario bruto es: {salario}")
#Mostrar los descuentos totales.
print(f"Los descuentos totales son: {descuentos}")
#Mostrar el salario neto.
print(f"El salario neto es: {salario_neto}")
#Fin del programa
