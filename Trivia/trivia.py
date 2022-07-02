
from clases import *

p1 = preguntas("alternativa", "¿Cuál fue el último disco que grabaron the Beatles?", ["The Beatles", "Yellow submarine","Let it be", "Abbey road"], ["a"], "El último disco que grabaron no fue el último disco que lanzaron.")
p2 = preguntas("múltiple", "¿Qué películas ganaron la mayor cantidad de premios Oscar?", ["Titanic", "El señor de los anillos: el retorno del rey", "lo que el viento se llevó","West side story"], ["a","b"],
               "La más viejas no lo son")
p3 = preguntas("alternativa", "¿Cuál es el nombre del cuñado de Michael Corleone?", ["Luca Brasi", "Pauli Gatto","Joey Zasa", "Carlo Rizzi"], ["d"], "Era amigo de Sony")
p4 = preguntas("corta", "¿Donde se realizará el próximo mundial de futbol? Escriba la respuesta en minúscula", ["qatar"], "Su capital es Doha")
p5 = preguntas("corta", "¿Cuántas hermanas tiene Joey Tribbiani? escriba solo el número", ["7"], "Es un número primo")
p6 = preguntas("múltiple", "¿Qué otros apodos recibe Jhon Wick? (seleccione dos alternativas)", ["la muerte", "Señor asesino", "Baba yaga","El hombre del saco"], ["c","d"],
               "Uno de los apodos corresponde a personaje del folclore eslavo")

nombre = input("Bienvenido a la trivia trivial, por favor escribe tu nombre: ")
print(f"hola {nombre} comenzamos con las preguntas:")
print()
p1.print()
p2.print()
p3.print()
p4.print()
p5.print()
p5.print()

print()
contador=p1.contador+p2.contador+p3.contador+p4.contador+p5.contador+p6.contador
print(f'Te equivocaste {contador} veces.')
print(f"Terminaste la trivia {nombre}, espero te hayas entretenido")




