#Cálculo del precio final de un producto con impuestos y descuentos
precio_original = float(input("Introduce el precio original del producto: "))
#Porcentaje de descuento a aplicar
descuento = float(input("Introduce el porcentaje de descuento: "))
#Multiplicar el precio por el porcentaje de descuento. 
descuento = precio_original * (descuento / 100)
precio_con_descuento = precio_original - descuento
#Ingresar el porcentaje de IVA a pagar
iva = float(input("Introduce el porcentaje de IVA: "))
#Multiplicar el precio con descuento por el porcentaje de IVA.
precio_final = precio_con_descuento * (iva / 100)
precio_final = precio_con_descuento + precio_final
#Mostrar el precio final del producto.  
print(f"El precio final del producto es: {precio_final:.2f} ")
