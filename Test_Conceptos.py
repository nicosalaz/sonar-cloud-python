import unittest
from TAP.TPA.Juego import Juego


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.nombreValido = "Prueba"
        self.definicionValida = "Una prueba es la definicion, salidas y procesos aprobados"
        self.nombreInvalido = "a"
        self.definicionInvalida = "no valido"
        self.nombreValidoInexistente = "Modelo"
        self.juego = Juego()

    def testAgregarConcepto(self):
        self.assertEqual(self.juego.agregarConcepto(self.nombreValido, self.definicionValida), True, "Agregar concepto nuevo")
        self.assertEqual(self.juego.agregarConcepto(self.nombreValido, self.definicionValida), False, "Agregar concepto existente")
        self.assertEqual(self.juego.agregarConcepto(self.nombreInvalido, self.definicionValida), False, "Agregar concepto con nombre invalido")
        self.assertEqual(self.juego.agregarConcepto(self.nombreValido, self.definicionInvalida), False, "Agregar concepto con definicion invalida")
        self.juego.configurarCantidadConceptosMostrar(self.juego.getCantidadConceptos())
        print(self.juego.presentarConceptos())

    def testBuscarConcepto(self):
        self.juego.agregarConcepto(self.nombreValido, self.definicionValida)
        self.assertEqual(self.juego.buscarConcepto(self.nombreValido), True, "Buscar concepto existente")
        self.assertEqual(self.juego.buscarConcepto(self.nombreValidoInexistente), False, "Buscar concepto inexistente")
        self.juego.configurarCantidadConceptosMostrar(self.juego.getCantidadConceptos())
        print(self.juego.presentarConceptos())

    def testEliminarConcepto(self):
        self.juego.agregarConcepto(self.nombreValido, self.definicionValida)
        self.assertEqual(self.juego.eliminarConcepto(self.nombreValido), True, "Eliminar concepto existente")
        self.assertEqual(self.juego.eliminarConcepto(self.nombreValidoInexistente), False, "Eliminar concepto inexistente")
        self.juego.configurarCantidadConceptosMostrar(self.juego.getCantidadConceptos())
        print(self.juego.presentarConceptos())


if __name__ == '__main__':
    unittest.main()
