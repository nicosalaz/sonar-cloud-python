from TAP.TPA.Jugador import Jugador


class InterfazJugador:

    def __init__(self, juego):
        self.juego = juego
        self.jugador = Jugador()

    def jugar(self):
        conceptosAcertados = 0
        estado = True
        print("### Para omitir algun concepto se debe usar la palabra clave: " + self.juego.getPalabraOmitir())
        print("Digite su nombre: ")
        nombre = input()
        while estado is True:
            msjConceptos = self.juego.presentarDefinicion()
            if len(msjConceptos) > 0:
                conceptosAcertados += self.validarRespuesta(msjConceptos)
            else:
                msjConceptosOmitidos = self.juego.presentarDefinicionOmitida()
                if len(msjConceptosOmitidos) > 0:
                    conceptosAcertados += self.validarRespuesta(msjConceptosOmitidos)
                else:
                    estado = False
        self.jugador.setNombreJugador(nombre)
        self.jugador.setCantidadConceptosAcertados(conceptosAcertados)
        print(self.jugador.getNombreJugador() + " acertaste " + str(self.jugador.getCantidadConceptosAcertados()) + " de " + str(self.juego.getCantidadConceptosMostrar()) + " conceptos")

    def validarRespuesta(self, msjConcepto):
        print(msjConcepto)
        respuesta = input()
        correcto = 0
        if self.juego.validarRespuestaConcepto(respuesta, msjConcepto) is True:
            correcto = 1
        return correcto
