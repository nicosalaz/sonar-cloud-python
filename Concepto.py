class Concepto:

    def __init__(self, nombre, definicion):
        self.nombre = nombre
        self.definicion = definicion
        self.omitido = False

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setDefinicion(self, definicion):
        self.definicion = definicion

    def getDefinicion(self):
        return self.definicion

    def setOmitido(self, estado):
        self.omitido = estado

    def getOmitido(self):
        return self.omitido

    def toString(self):
        informacion = "\tNombre: " + self.nombre + "\n\tDefinicion: " + self.definicion
        return informacion
