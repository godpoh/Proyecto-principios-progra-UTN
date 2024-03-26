class GestionJugadores:
    def __init__(self):
        self.jugadores = []

    def menu_principal(self):
        while True:
            print("\n------------Menu Principal------------")
            print("1-Gestion de Jugadores")
            print("2-Visualizar lista de jugadores")
            print("3-Estadísticas de Jugadores")
            print("4-Consultas avanzadas")
            print("5-Salir del sistema.")
            print("--------------------------------------")
            opciones = input("Ingrese el digito de la opcion(1-5)")

            if opciones == '1':
                self.gestion_jugadores()
            elif opciones == '2':
                self.ver_lista_jugadores()
            elif opciones == '3':
                self.estadisticas_jugadores()
            elif opciones == '4':
                self.consultas_avanzadas()
            elif opciones == '5':
                break
            else:
                print("Valor no valido, vuelva a intentarlo")

    #Menu principal Menu principal Menu principal Menu principal Menu principal Menu principal
    def gestion_jugadores(self):
        while True:
            print("\n--- Gestion de Jugadores ---")
            print("1-Insertar un nuevo jugador")
            print("2-Leer informacion de un jugador")
            print("3-Modificar datos de un jugador")
            print("4-Eliminar un jugador de la base de datos")
            print("5-Regresar al menu principal")

            opciones = input("Ingrese el digito de la opcion(1-5)")

            if opciones == '1':
                self.insertar_jugador()
            elif opciones == '2':
                self.leer_informacion_jugador()
            elif opciones == '3':
                self.modificar_datos_jugador()
            elif opciones == '4':
                self.eliminar_jugador()
            elif opciones == '5':
                break
            else:
                print("Valor no valido, vuelva a intentarlo")

    def visualizar_lista_jugadores(self):
        pass

    def estadisticas_jugadores(self):
        pass

    def consultas_avanzadas(self):
        pass

    #Gestion de jugadores Gestion de jugadores Gestion de jugadores Gestion de jugadores

    def insertar_nuevo_jugador(self):
        pass

    def leer_informacion_jugador(self):
        pass

    def modificar_datos_jugador(self):
        pass

    def eliminar_jugador(self):
        pass

prueba = GestionJugadores()
prueba.menu_principal()

