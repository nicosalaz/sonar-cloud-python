class Configuracion:

    def __init__(self, tiempo=0, cantidad=0, palabra="omitir"):
        self.tiempoJuego = tiempo
        self.cantidadPreguntas = cantidad
        self.palabraOmitir = palabra

    def setTiempoJuego(self, tiempo):
        self.tiempoJuego = tiempo

    def getTiempoJuego(self):
        return self.tiempoJuego

    def setCantidadConceptosMostrar(self, cantidad):
        self.cantidadPreguntas = cantidad

    def getCantidadConceptosMostrar(self):
        return self.cantidadPreguntas

    def setPalabraOmitir(self, palabra):
        self.palabraOmitir = palabra

    def getPalabraOmitir(self):
        return self.palabraOmitir
