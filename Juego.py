from TAP.TPA.Configuracion import Configuracion
from TAP.TPA.Concepto import Concepto


class Juego:

    def __init__(self, valor=1):
        self.configuracion = Configuracion()
        self.conceptos = list()
        self.valorConceptoAcertado = valor
        self.conceptoActual = 0

    def getCantidadConceptos(self):
        return len(self.conceptos)

    def agregarConcepto(self, nombre, definicion):
        if len(nombre) > 1 and len(definicion) > 5 and self.buscarConcepto(nombre) is False:
            concepto = Concepto(nombre, definicion)
            self.conceptos.append(concepto)
            estado = True
        else:
            estado = False
        return estado

    def eliminarConcepto(self, nombre):
        estado = False
        if self.buscarConcepto(nombre) is True:
            self.conceptos.pop(self.getPosConcepto(nombre))
            estado = True
        return estado

    def getPosConcepto(self, nombre):
        posConcepto = -1
        for concepto in self.conceptos:
            posConcepto += 1
            if concepto.getNombre() == nombre:
                break
        return posConcepto

    def buscarConcepto(self, nombre):
        estado = False
        for concepto in self.conceptos:
            if concepto.getNombre() == nombre:
                estado = True
                break
        return estado

    def getConcepto(self, nombre):
        conceptoEncontrado = None
        for concepto in self.conceptos:
            if concepto.getNombre() == nombre:
                conceptoEncontrado = concepto
                break
        return conceptoEncontrado

    def getConceptoId(self, id):
        conceptoEncontrado = None
        for concepto in range(len(self.conceptos)):
            if concepto == id:
                conceptoEncontrado = self.conceptos[concepto]
                break
        return conceptoEncontrado

    def configurarTiempo(self, tiempo):
        estado = False
        if tiempo > 0:
            self.configuracion.setTiempoJuego(tiempo)
            estado = True
        return estado

    def getTiempoJuego(self):
        return self.configuracion.getTiempoJuego()

    def configurarPalabraOmitir(self, palabra):
        estado = False
        if len(palabra) > 0:
            self.configuracion.setPalabraOmitir(palabra)
            estado = True
        return estado

    def getPalabraOmitir(self):
        return self.configuracion.getPalabraOmitir()

    def configurarCantidadConceptosMostrar(self, cantidad):
        estado = False
        if 0 < cantidad <= len(self.conceptos):
            self.configuracion.setCantidadConceptosMostrar(cantidad)
            estado = True
        return estado

    def getCantidadConceptosMostrar(self):
        return self.configuracion.getCantidadConceptosMostrar()

    def validarRespuestaConcepto(self, respuesta, definicionPresentada):
        estado = False
        if self.buscarConcepto(respuesta) or respuesta == self.configuracion.getPalabraOmitir():
            for concepto in self.conceptos:
                if definicionPresentada == concepto.getDefinicion():
                    if respuesta == concepto.getNombre():
                        estado = True
                    elif respuesta == self.configuracion.getPalabraOmitir():
                        concepto.setOmitido(True)
                        estado = None
                    break
        return estado

    def presentarDefinicionOmitida(self):
        definicion = ""
        for concepto in range(0, len(self.conceptos)):
            if self.conceptos[concepto].getOmitido() is True:
                definicion = self.conceptos[concepto].getDefinicion()
                self.conceptos[concepto].setOmitido(False)
                break
        return definicion

    def presentarDefinicion(self):
        definicion = ""
        for concepto in range(self.conceptoActual, self.configuracion.getCantidadConceptosMostrar()):
            if self.conceptos[concepto].getOmitido() is False:
                definicion = self.conceptos[concepto].getDefinicion()
                self.conceptoActual += 1
                break
        return definicion

    def presentarConceptos(self):
        if self.configuracion.getCantidadConceptosMostrar() > 0:
            informacion = "#CONCEPTOS\n"
        else:
            informacion = "No hay conceptos"
        for concepto in range(0, self.getCantidadConceptos()):
            informacion += str(concepto + 1) + "." + self.conceptos[concepto].toString() + "\n"
        return informacion
