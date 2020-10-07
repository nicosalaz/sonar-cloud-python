class Jugador:

    def __init__(self, nombre=None):
        self.nombreJugador = nombre
        self.puntaje = 0
        self.tiempo = 0
        self.cantidadConceptosAcertados = 0

    def setNombreJugador(self, nombre):
        self.nombreJugador = nombre

    def getNombreJugador(self):
        return self.nombreJugador

    def setPuntaje(self, puntaje):
        self.puntaje = puntaje

    def getPuntaje(self):
        return set.puntaje

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def setCantidadConceptosAcertados(self, cantidad):
        self.cantidadConceptosAcertados = cantidad

    def getCantidadConceptosAcertados(self):
        return self.cantidadConceptosAcertados
