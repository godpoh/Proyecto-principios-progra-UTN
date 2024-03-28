import json
import time

class Menu:
    def __init__(self):
        self.opciones_principales = {
            '1': self.gestion_jugadores,
            '2': self.visualizar_lista_jugadores,
            '3': self.estadisticas_jugadores,
            '4': self.consultas_avanzadas,
            '5': self.salir
        }

    def mostrar_menu_principal(self):

        print("\n------------Menu Principal------------")
        print("1-Gestion de Jugadores")
        print("2-Visualizar lista de jugadores")
        print("3-Estadísticas de Jugadores")
        print("4-Consultas avanzadas")
        print("5-Salir del sistema.")
        print("--------------------------------------")

    #Menu principal Menu principal Menu principal Menu principal Menu principal Menu principal
    def gestion_jugadores(self):
        while True:
            print("\n------------Gestion de Jugadores------------")
            print("1-Insertar un nuevo jugador")
            print("2-Leer informacion de un jugador")
            print("3-Modificar datos de un jugador")
            print("4-Eliminar un jugador de la base de datos")
            print("5-Regresar al menu principal")
            print("--------------------------------------------")
            opciones = input("Ingrese el digito de la opcion(1-5): ")

            if opciones == '1':
                self.insertar_nuevo_jugador()
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
        try:
            with open("jugadores.json", "r") as file:
                jugadores_datos = json.load(file)
                print(json.dumps(jugadores_datos, indent=4))
        except FileNotFoundError:
            print("El archivo 'jugadores.json' no se encontró.")
        except json.JSONDecodeError:
            print("El archivo 'jugadores.json' no contiene datos JSON válidos.")
        while True:
            opcion = input("¿Desea volver al menú principal? (SI): ")
            if opcion.lower() == 'si':
                print("Volviendo al menú principal.")
                time.sleep(2)
                return
            else:
                print("Por favor, digite 'SI'.")

    def estadisticas_jugadores(self):
        with open("estadistica_jugador.json", "r") as file:
            datos_estadisticas = json.load(file)
            print(json.dumps(datos_estadisticas, indent=4))
        while True:
            opcion = input("Desea volver al menu principal?(SI): ")
            if opcion.lower() == 'si':
                print("Volviendo al menu principal")
                time.sleep(2)
                return()

    def consultas_avanzadas(self):
        pass

    def salir(self):
        print("Saliendo del sistema.")
        exit()

    def main(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones_principales.get(opcion)
            if accion:
                accion()
            else:
                print("\nError: Opción no válida. Por favor, seleccione una opción válida.\n")

#Gestion de jugadores Gestion de jugadores Gestion de jugadores Gestion de jugadores

    def insertar_nuevo_jugador(self):
        pass

    def leer_informacion_jugador(self):
        pass

    def modificar_datos_jugador(self):
        pass

    def eliminar_jugador(self):
        pass

#CONSULTAS AVANZADAS #CONSULTAS AVANZADAS #CONSULTAS AVANZADAS #CONSULTAS AVANZADAS #CONSULTAS AVANZADAS

    def Mostrar_cantidad_jugadores_mismo_origen(self):
        pass

    def Mostrar_todos_los_jugadores_que_se_encuentren_en_un_rango_de_edad(self):
        pass

    def Mostrar_cantidad_jugadores_con_misma_altura_y_tienen_referencia_al_género_de_cada_uno(self):
        pass

    def Mostrar_los_jugadores_de_Club_específico(self):
        pass
    def Mostrar_cantidad_jugadores_acuerdo_con_la_posición_en_el_campo_considerando_unicamente_los_de_género_femenino(self):
        pass
    def Mostrar_top_diez_jugadores_mayor_altura_con_mejor_agilidad_la_información_muestra_nombre_genero_origen_altura_agilidad(self):
        pass
    def Mostrar_cantidad_jugadores_cuya_velocidad_este_en_un_rango_específico(self):
        pass
    def Determinar_promedio_control_balon_para_jugadores_en_una_posición_específica(self):
        pass


iniciador = Menu()
iniciador.main()