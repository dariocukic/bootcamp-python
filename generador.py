import random
import math

def leer_numero(i, f, m):
    print(m)
    a = int(input())
    while a < i or a > f:
        print("La opción no es válida")
        print(m)
        a = int(input())
    return a

def generador():
    numeros = leer_numero(1, 20, "¿Cuántos números quieres generar?[1-20]: ")
    modo = leer_numero(1, 3, '¿Cómo quieres redondear los números? [1] Al alza, [2] a la baja o [3] normal ')

    lista = [0] * numeros
    print(lista)
    for n in range(numeros):
        lista[n] = random.uniform(0, 100)

    lista_aprox = [0] * numeros
    for n in range(numeros):
        if modo == 1:
            lista_aprox[n] = math.ceil(lista[n])
        elif modo == 2:
            lista_aprox[n] = math.floor(lista[n])
        else:
            lista_aprox[n] = round(lista[n])

    return print(f'Lista sin aprox: {lista} \nLista aprox: {lista_aprox}')

generador()