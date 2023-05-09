ingreso_mensual = 30000
gasto_mensual = 10000

#if anidados y else if (elif)
 
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deificit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else:
        print("estas gastando mas")
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
else:
    print("no te alcanza para nada")