class preguntas(object):
    def __init__(self, tipo: str, pregunta: str, alternativas: list, correcta: list, pista: str):
        self.tipo = tipo
        self.pregunta = pregunta
        self.alternativas = alternativas
        self.correcta = correcta
        self.pista = pista

    def tipo(self):  # guarda el tipo
        print(self.tipo)

    def pregunta(self):  # guarda la pregunta
        print(self.pregunta)

    def correcta(self):  # guarda la alternativa correcta
        print(self.correcta)

    def alternativas(self):  # guarda las alternativas de cada pregunta
        print(self.alternativas)

    def pista(self):  # guarda la pista de cada pregunta
        print(self.pista)

    def contador(self):  #contador para indicar cuántas incorrectas hay
        print(self.contador)

    def print(self):  # me permite mandar a pantalla las preguntas de acuerdo al tipo de pregunta
        self.contador = 0
        if self.tipo == "alternativa":
            print(f"{self.pregunta}")
            print(f"a) {self.alternativas[0]}")
            print(f"b) {self.alternativas[1]}")
            print(f"c) {self.alternativas[2]}")
            print(f"d) {self.alternativas[3]}")

            resp = "z"  # Esto funciona para tipo alternativas
            while resp != self.correcta[0]:
                resp = input("Ingrese la alternativa correcta: ")
                if resp != "a" and resp != "b" and resp != "c" and resp != "d":
                    print("solo puede elegir las opciones a, b, c o d")
                    print()
                elif resp == self.correcta[0]:
                    print("bien")
                else:
                    print("mal, intentalo de nuevo")
                    self.contador = self.contador + 1
                    print()
                    print(f"Te dejo una pista: {self.pista} ")
                    print()
            print()

        elif self.tipo == "multiple":  # Esto para tipo alternativas con respuestas múltiples... solo 2 respuestas hasta el momento
            print(f"{self.pregunta}")
            print(f"a) {self.alternativas[0]}")
            print(f"b) {self.alternativas[1]}")
            print(f"c) {self.alternativas[2]}")
            print(f"d) {self.alternativas[3]}")

            resp = ["z", "z"]
            while resp != [self.correcta[0], self.correcta[1]] and resp != [self.correcta[1], self.correcta[0]]:
                resp[0] = input("Escriba la 1ra alternativa correcta: ")
                resp[1] = input("Escriba la 2da alternativa correcta:")
                if resp[0] != "a" and resp[0] != "b" and resp[0] != "c" and resp[0] != "d":
                    print("solo puede elegir las opciones a, b, c o d")
                    print()
                elif resp[1] != "a" and resp[1] != "b" and resp[1] != "c" and resp[1] != "d":
                    print("solo puede elegir las opciones a, b, c o d")
                    print()
                elif resp[0] == resp[1]:
                    print("Colocaste la misma respuesta dos veces")
                    print()
                elif resp[0] == self.correcta[0] and resp[1] == self.correcta[1]:
                    print("bien")
                elif resp[1] == self.correcta[0] and resp[0] == self.correcta[1]:
                    print("bien")
                else:
                    self.contador = self.contador + 1
                    print("mal, intentalo de nuevo")
                    print()
                    print(f"Te dejo una pista: {self.pista} ")
                    print()
            print()

        elif self.tipo == "corta":  # Esta para respuesta corta
            print(f"{self.pregunta}")
            resp = "z"
            while resp != self.correcta[0]:
                resp = input("Escriba la respuesta correcta, en minúsculas: ")
                if resp == self.correcta[0]:
                    print("bien")
                else:
                    self.contador = self.contador + 1
                    print("mal, intentalo de nuevo")
                    print()
                    print(f"Te dejo una pista: {self.pista} ")
                    print()

        else:  # Esto está por si hay un error al cargar la pregunta
            print("EEEHHH")