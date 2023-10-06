factura_total = float(input("¿Cuál es la factura total de hoy? $"))
porcentaje_propina = float(input("¿Qué porcentaje de propina deseas dar? (18, 20, o 25): "))

propina = factura_total * (porcentaje_propina / 100)
total_con_propina = factura_total + propina

print(f"La propina aplicando el {porcentaje_propina}% es ${round(propina, 2)}, que contabiliza un total de ${round(total_con_propina, 2)}")