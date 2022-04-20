ci=float(input("Ingrese el monto a invertir:"))
i=float(input("Ingrese el interés anual (solo el número):"))
n=float(input("Ingrese el tiempo en años:"))
cf=ci*(1+i/100)**n

print("El capital obtenido en la inversión es: "+str(cf))






