import json
import time

class agregar_jugadores:
    def __init__(self, nombre, fecha_de_nacimiento, origen, genero, altura, peso, posicion_campo, club_militante, reconocimientos):
        self.nombre = []

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
                print("Volviendo al menu principal")
                time.sleep(2)
                return
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

    import json

    def insertar_nuevo_jugador(self):
        while True:
            # Solicitar al usuario que ingrese los datos del nuevo jugador

            nombre = input("Ingrese el nombre del jugador (Ej: Jose Maria): ")
            if nombre.replace(" ", "").isalpha():
                pass
            else:
                print("\nError: El nombre debe contener solo letras.")
                continue

            fecha_nacimiento = input("Ingrese la fecha de nacimiento del jugador (Ej: 28 de octubre de 1991): ")

            origen = input("Ingrese el origen del jugador (Ej: Costa Rica): ")
            if origen.replace(" ", "").isalpha():
                pass
            else:
                print("\nError: El nombre debe contener solo letras.")
                continue

            genero = input("Ingrese el género del jugador (Masculino/Femenino): ")
            if not genero.isalpha():
                print("\nError: El genero debe contener solo letras")
            if not (genero == "Masculino" or genero == "Femenino"):
                print("\nError: Debe ser Masculino o Femenino")
                continue

            altura = input("Ingrese la altura del jugador (Ej: 1.82): ")
            try:
                altura = float(altura)
                if altura < 1 or altura > 2.1:
                    print("\nError: Debe ser una altura entre 1.0 y 2.0")
            except ValueError:
                print("\nError: La altura debe ser un número decimal y debe llever un(.)")
                continue

            peso = input("Ingrese el peso del jugador (Ej: 82.5kgs): ")
            try:
                peso = float(peso)
                if peso < 50 or peso > 200:
                    print("\nError: Debe ser un peso entre 50 y 120kgs")
            except ValueError:
                print("\nError: El peso debe ser un número decimal y debe llever un(.)")
                continue

            posicion_campo = input("Ingrese la posición en el campo del jugador (Ej: Delantero): ")
            try:
                posicion_campo = str(posicion_campo)
            except ValueError:
                print("\nError: La posicion del campo debe ser solo letras")

            club_militante = input("Ingrese el club militante del jugador (Ej: Inter Miami): ")
            if club_militante.replace(" ", "").isalpha():
                pass
            else:
                print("\nError: Debe contener solo letras.")
                continue

            reconocimientos = input("Ingrese los reconocimientos del jugador (Ej: 13): ")
            try:
                reconocimientos = int(reconocimientos)
            except ValueError:
                print("\nError: Los reconocimientos deben ser un número entero.")
                continue

            idx = input("Ingrese el ID del jugador (Ej: 30): ")

            jugador = input("Ingrese el nombre del jugador nuevamente (Debe ser exactamente igual): ")
            if not jugador == nombre:
                print("\nError: El nombre del jugador debe de ser el mismo")
                continue

            aceleracion = input("Ingrese la aceleracion del jugador (Ej: 1-99): ")
            try:
                aceleracion = int(aceleracion)
                if aceleracion < 0 or aceleracion > 100:
                    print("\nError: El valor debe estar en el rango de 0 a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            pases_cortos = input("Ingrese la estadistica de pases cortos del jugador(Ej: 1-99): ")
            pases_cortos = int(pases_cortos)
            try:
                if pases_cortos < 0 or pases_cortos > 100:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            potencia_tiro = input("Ingrese la potencia de tiro del jugador (Ej: 1-99): ")
            potencia_tiro = int(potencia_tiro)
            try:
                if potencia_tiro < 0 or potencia_tiro > 100:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            pases_largos = input("Ingrese la estadistica de pases largos del jugador(Ej: 1-99): ")
            pases_largos = int(pases_largos)
            try:
                if pases_largos < 0 or pases_largos > 100:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            velocidad = input("Ingrese la velocidad del jugador(Ej: 1-99): ")
            velocidad = int(velocidad)
            try:
                if velocidad < 0 or velocidad > 100:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            agilidad = input("Ingrese la agilidad del jugador(Ej: 1-99): ")
            agilidad = int(agilidad)
            try:
                if agilidad < 0 or agilidad > 100:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            resistencia = input("Ingrese la resistencia del jugador(Ej: 1-99): ")
            resistencia = int(resistencia)
            try:
                if resistencia < 0 or resistencia > 100:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            salto = input("Ingrese el salto del jugador(Ej: 1-99): ")
            salto = int(salto)
            try:
                if salto < 0 or salto > 100:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            regates = input("Ingrese la estadistica de regate del jugador(Ej: 1-99): ")
            regates = int(regates)
            try:
                if regates < 0 or regates > 100:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue
            control_balon = input("Ingrese la estadistica de control de balon del jugador(Ej: 1-99): ")
            control_balon = int(control_balon)
            try:
                if control_balon < 0 or control_balon > 100:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            # Crear un diccionario con los datos del nuevo jugador
            nuevo_jugador = {
                "nombre": nombre,
                "fecha_nacimiento": fecha_nacimiento,
                "origen": origen,
                "genero": genero,
                "altura": altura,
                "peso": peso,
                "posicion_campo": posicion_campo,
                "club_militante": club_militante,
                "reconocimientos": reconocimientos
            }

            nuevo_jugador_estadisticas = {
                "ID": idx,
                "Jugador": jugador,
                "Aceleracion": aceleracion,
                "Pases cortos": pases_cortos,
                "Potencia de tiro": potencia_tiro,
                "Pases largos": pases_largos,
                "Velocidad": velocidad,
                "Agilidad": agilidad,
                "Resistencia": resistencia,
                "Salto": salto,
                "Regates": regates,
                "Control de balon": control_balon
            }

            # Leer los datos actuales de los jugadores desde el archivo JSON
            try:
                with open("jugadores.json", "r") as file:
                    jugadores = json.load(file)
            except FileNotFoundError:
                jugadores = []

            # Agregar el nuevo jugador a la lista de jugadores
            jugadores.append(nuevo_jugador)

            # Escribir los datos actualizados de los jugadores en el archivo JSON
            with open("jugadores.json", "w") as file:
                json.dump(jugadores, file, indent=4)

            try:
                with open("estadistica_jugador.json", "r") as file:
                    estadistica = json.load(file)
            except FileNotFoundError:
                estadistica = []

            estadistica.append(nuevo_jugador_estadisticas)

            with open("estadistica_jugador.json", "w") as file:
                json.dump(estadistica, file, indent=4)

            print("Nuevo jugador agregado con éxito.")
            time.sleep(2)
            return()


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