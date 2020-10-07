class InterfazAdmin:

    def __init__(self, juego):
        self.juego = juego

    def menu(self):
        opcion = 0
        print("Menu")
        print("1. Conceptos")
        print("2. Configuracion")
        print("3. Volver")
        while opcion < 1 or opcion > 3:
            print("Seleccione una opcion")
            opcion = int(input())
        self.opcionesMenu(opcion)

    def opcionesMenu(self, opcion):
        if opcion == 1:
            self.menuConceptos()
        elif opcion == 2:
            self.menuConfiguracion()

    def menuConceptos(self):
        opcion = 0
        print("Menu de conceptos")
        print("1. Agregar concepto")
        print("2. Eliminar concepto")
        print("3. Buscar concepto")
        print("4. Volver")
        while opcion < 1 or opcion > 4:
            print("Seleccione una opcion")
            opcion = int(input())
        self.opcionesMenuConceptos(opcion)

    def opcionesMenuConceptos(self, opcion):
        if opcion == 1:
            self.agregarConcepto()
        elif opcion == 2:
            self.eliminarConcepto()
        elif opcion == 3:
            self.buscarConcepto()
        elif opcion == 4:
            self.menu()

    def agregarConcepto(self):
        estado = False
        while estado is False:
            print("Digite el nombre del concepto")
            nombre = input()
            print("Digite la definicion del concepto")
            definicion = input()
            if self.juego.agregarConcepto(nombre, definicion) is True:
                estado = True
            else:
                print("El concepto no es valido o ya existe")
        self.menuConceptos()

    def eliminarConcepto(self):
        opcion = 0
        while opcion < 1 or opcion > self.juego.getCantidadConceptos():
            print("Seleccione el concepto que desea eliminar\n" + self.juego.presentarConceptos())
            opcion = int(input())
        self.juego.eliminarConcepto(self.juego.getConceptoId(opcion - 1).getNombre())
        self.menuConceptos()

    def buscarConcepto(self):
        print("Digite el nombre del concepto que desea buscar")
        nombre = input()
        if self.juego.buscarConcepto(nombre) is True:
            print(self.juego.getConcepto(nombre).toString())
        else:
            print("El concepto no se ha encontrado")
        self.menuConceptos()

    def menuConfiguracion(self):
        opcion = 0
        print("Menu de configuracion")
        print("1. Tiempo por juego")
        print("2. Cantidad de conceptos a presentar")
        print("3. Palabra clave para omitir conceptos")
        print("4. Volver")
        while opcion < 1 or opcion > 4:
            print("Seleccione una opcion")
            opcion = int(input())
        self.opcionesMenuConfiguracion(opcion)

    def opcionesMenuConfiguracion(self, opcion):
        if opcion == 1:
            self.configurarTiempo()
        elif opcion == 2:
            self.configurarCantidadConceptos()
        elif opcion == 3:
            self.configurarPalabraOmitir()
        elif opcion == 4:
            self.menu()

    def configurarTiempo(self):
        estado = False
        while estado is False:
            print("Digite la duracion del juego en minutos")
            tiempo = int(input())
            if self.juego.configurarTiempo(tiempo) is True:
                estado = True
            else:
                print("Duracion invalida")
        self.menuConfiguracion()

    def configurarCantidadConceptos(self):
        estado = False
        while estado is False:
            print("Digite la cantidad de conceptos que se mostraran")
            cantidad = int(input())
            if self.juego.configurarCantidadConceptosMostrar(cantidad) is True:
                estado = True
            else:
                print("Cantidad invalida, se pueden mostrar como maximo " + str(self.juego.getCantidadConceptos()) + " conceptos")
        self.menuConfiguracion()

    def configurarPalabraOmitir(self):
        estado = False
        while estado is False:
            print("Digite la palabra clave para omitir conceptos")
            palabraOmitir = input()
            if self.juego.configurarPalabraOmitir(palabraOmitir) is True:
                estado = True
            else:
                print("Palabra invalida")
        self.menuConfiguracion()
