# Calculadora de propinas:

# - Pide el total de la factura
# - Pregunta que porcentaje de propina quiere dar 10, 12 0 15%
# - Pregunta entre cuántas personas se repartiran la cuenta
# - Muestra cuanto debe pagar cada persona

print("\n¡Bienvenido a la calculadora de propinas!\n")

factura = float(input("Ingresa el total de la factura: $"))
propina = int(input("¿Que porcentaje de propina le gustaria dar 10, 12 o 15?: "))
personas = int(input("Entre cuantas personas se repartirá la cuenta: "))

pago_por_persona = factura * (propina / 100 + 1) / personas
print(f"Cada persona debe pagar: ${pago_por_persona:.2f} pesos.")

