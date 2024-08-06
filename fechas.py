meses = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4,'Mayo': 5, 'Junio': 6, 'Julio': 7, 'Agosto': 8,
         'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}
fecha_ingresada=input("ingrese fecha en formato Dia,Mes Año:")
    
    # Separar la fecha en partes
partes = fecha_ingresada.split(', ')
    
    # Extraer el día y el mes con el año
dia = partes[0]
mes_y_año = partes[1].split(' ')
    
    # Extraer el nombre del mes y el año
mes = mes_y_año[0]
año = mes_y_año[1]
    
    # Convertir el nombre del mes a número
mes_numero = meses[mes]
    
    # Imprimir la fecha en formato numérico
print(f"{dia} {mes_numero} {año}")