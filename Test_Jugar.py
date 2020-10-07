import unittest
from Juego import Juego

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.juego = Juego()
        self.juego.agregarConcepto("Uno", "Uno, numero valido")
        self.juego.agregarConcepto("Dos", "Dos, numero valido")
        self.juego.agregarConcepto("Tres", "Tres, numero valido")
        self.juego.agregarConcepto("Cuatro", "Cuatro, numero valido")
        self.juego.configurarCantidadConceptosMostrar(self.juego.getCantidadConceptos())

    def testResponderCorrectamente(self):
        print(self.juego.presentarConceptos())
        self.assertEqual(self.juego.validarRespuestaConcepto("Uno", self.juego.presentarDefinicion()), True, "Respondiendo correctamente")
        self.assertEqual(self.juego.validarRespuestaConcepto("Dos", self.juego.presentarDefinicion()), True, "Respondiendo correctamente")

    def testResponderIncorrectamente(self):
        print(self.juego.presentarConceptos())
        self.assertEqual(self.juego.validarRespuestaConcepto("Dos", self.juego.presentarDefinicion()), False, "Respondiendo incorrectamente")
        print("Siguiente concepto: " + self.juego.presentarDefinicion())

    def testOmitir(self):
        self.assertEqual(self.juego.validarRespuestaConcepto(self.juego.getPalabraOmitir(), self.juego.presentarDefinicion()), None, "Omitiendo el concepto")
        print("Definicion: " + self.juego.presentarDefinicionOmitida() + " -> pablabraOmitir: " + self.juego.getPalabraOmitir())

    def testTodoCorrecto(self):
        self.assertEqual(self.juego.validarRespuestaConcepto("Uno", self.juego.presentarDefinicion()), True, "Respondiendo correctamente")
        self.assertEqual(self.juego.validarRespuestaConcepto("Dos", self.juego.presentarDefinicion()), True, "Respondiendo correctamente")
        self.assertEqual(self.juego.validarRespuestaConcepto("Tres", self.juego.presentarDefinicion()), True, "Respondiendo correctamente")
        self.assertEqual(self.juego.validarRespuestaConcepto("Cuatro", self.juego.presentarDefinicion()), True, "Respondiendo correctamente")


if __name__ == '__main__':
    unittest.main()
