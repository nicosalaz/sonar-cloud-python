import unittest
from TAP.TPA.Juego import Juego


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cantidadPreguntasValidaSuperior = 4
        self.cantidadPreguntasValidaInferior = 1
        self.juego = Juego()
        self.juego.agregarConcepto("Uno", "Uno, numero valido")
        self.juego.agregarConcepto("Dos", "Dos, numero valido")
        self.juego.agregarConcepto("Tres", "Tres, numero valido")
        self.juego.agregarConcepto("Cuatro", "Cuatro, numero valido")

    def testConfigurarTiempo(self):
        tiempoJuegoValido = 5
        tiempoJuegoInvalido = 0
        self.assertEqual(self.juego.configurarTiempo(tiempoJuegoValido), True, "Configurar tiempo de juego valido")
        self.assertEqual(self.juego.configurarTiempo(tiempoJuegoInvalido), False, "Configurar tiempo de juego invalido")

    def testConfigurarCantidadPreguntas(self):
        self.assertEqual(self.juego.configurarCantidadConceptosMostrar(self.cantidadPreguntasValidaSuperior), True, "Configurar cantidad de preguntas a mostrar valida, limite superior")
        print(self.juego.presentarConceptos())
        self.assertEqual(self.juego.configurarCantidadConceptosMostrar(self.cantidadPreguntasValidaInferior), True, "Configurar cantidad de preguntas a mostrar valida, limite inferior")
        print(self.juego.presentarConceptos())
        self.assertEqual(self.juego.configurarCantidadConceptosMostrar(self.cantidadPreguntasValidaSuperior + 1), False, "Configurar cantidad de preguntas a mostrar invalida, limite superior")
        self.assertEqual(self.juego.configurarCantidadConceptosMostrar(self.cantidadPreguntasValidaInferior - 1), False, "Configurar cantidad de preguntas a mostrar invalida, limite inferior")
        print(self.juego.presentarConceptos())

    def testConfigurarPalabraOmitir(self):
        palabraOmitir = "N/A"
        self.juego.configurarCantidadConceptosMostrar(self.cantidadPreguntasValidaSuperior)
        self.assertEqual(self.juego.validarRespuestaConcepto("omitir", self.juego.presentarDefinicion()), None, "Prueba palabra omitir por defecto")
        print("Definicion: " + self.juego.presentarDefinicionOmitida() + " -> palabraOmitir: " + self.juego.getPalabraOmitir())
        self.assertEqual(self.juego.configurarPalabraOmitir(palabraOmitir), True, "Configurar nueva palabra omitir")
        self.assertEqual(self.juego.validarRespuestaConcepto(palabraOmitir, self.juego.presentarDefinicion()), None, "Prueba nueva palabra omitir")
        print("Definicion: " + self.juego.presentarDefinicionOmitida() + " -> palabraOmitir: " + self.juego.getPalabraOmitir())
        self.assertEqual(self.juego.validarRespuestaConcepto("o", self.juego.presentarDefinicion()), False, "Prueba palabra omitir por defecto")
        print("Definicion: " + self.juego.presentarDefinicionOmitida() + " -> palabraOmitir: " + self.juego.getPalabraOmitir())


if __name__ == '__main__':
    unittest.main()
