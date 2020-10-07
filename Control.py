from TAP.TPA.Juego import Juego
from TAP.TPA.InterfazJugador import InterfazJugador
from TAP.TPA.InterfazAdmin import InterfazAdmin


class Control:

    def __init__(self):
        self.juego = Juego()
        #self.valoresPrueba()
        self.IJ = InterfazJugador(self.juego)
        self.IA = InterfazAdmin(self.juego)

    def valoresPrueba(self):
        self.juego.agregarConcepto("Uno", "Uno, numero valido")
        self.juego.agregarConcepto("Dos", "Dos, numero valido")
        self.juego.agregarConcepto("Tres", "Tres, numero valido")
        self.juego.agregarConcepto("Cuatro", "Cuatro, numero valido")
        self.juego.configurarCantidadConceptosMostrar(self.juego.getCantidadConceptos())

    def menu(self):
        opcion = 0
        print("MENU PRINCIPAL")
        print("1. Jugar")
        print("2. Administrar juego")
        print("3. Salir")
        while opcion < 1 or opcion > 3:
            print("Seleccione una opcion")
            opcion = int(input())
        self.opcionesMenu(opcion)

    def opcionesMenu(self, opcion):
        if opcion == 1:
            if self.juego.getCantidadConceptos() > 0:
                self.IJ.jugar()
            else:
                print("No hay ningun concepto o no se ha configurado la cantidad de conceptos a mostrar & el tiempo de juego")
            self.menu()
        elif opcion == 2:
            self.IA.menu()
            self.menu()
