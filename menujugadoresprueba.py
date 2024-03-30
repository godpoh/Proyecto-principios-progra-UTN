import json
import time
import re

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
        while True:
            print("\nSeleccione un filtro para visualizar la lista de jugadores")
            print("1-Por posicion de campo")
            print("2-Por origen(PAIS)")
            print("3-Por reconocimientos(BALONES DE ORO, ETC)")
            print("4-Mostrar todos los jugadores")
            print("5-Regresar al Menu Principal")
            print("----------------------------------------------------------")

            opcion = input("Ingrese el numero de la opcion deseada: ")

            if opcion == '1':
                self.filtrar_por_posicion_campo()
            elif opcion == '2':
                self.filtrar_por_origen()
            elif opcion == '3':
                self.filtrar_por_reconocimientos()
            elif opcion == '4':
                self.visualizar_todos_jugadores()
            elif opcion == '5':
                print("Volviendo al menu principal")
                time.sleep(2)
                return
            else:
                print("Opcion invalida, porfavor seleccione una opcion valida.")

    def filtrar_por_posicion_campo(self):
        while True:
            print("IMPORTANTE: Deben ser solo LETRAS, ademas ambas iniciales deben empezar con MAYUSCULAS ej: Delantero o Extremo Derecho.")
            filtrar = input("Ingrese la posicion que desea filtrar de los jugadores: ")
            if not filtrar.isalpha() or not filtrar.istitle():
                continue
            try:
                with open("jugadores.json", "r") as jugadores_file:
                    jugadores = json.load(jugadores_file)
#esta primera (jugador_expresion) es una variable de iteracion que se utiliza para recorrer cada elemento de la lista jugadores.
                    filtrar_jugadores = [jugador_expresion for jugador_expresion in jugadores if jugador_expresion["posicion_campo"] == filtrar]
                    if jugadores:
                        print("Jugadores encontrados: ")
                        for jugador_expresion in filtrar_jugadores:
                            print(json.dumps(jugador_expresion, indent=4))
                        opcion = input("Desea realizar otra consulta? (SI/NO): ")
                        if opcion.lower() != 'si':
                            print("Volviendo al menu anterior...")
                            time.sleep(2)
                            break
                    else:
                        print("No se encontraron jugadores de la posicion especificida")

            except FileNotFoundError:
                print("No existe el archivo")
            except json.decoder.JSONDecodeError:
                print("El archivo jugadores.json no contiene datos legibles")

    def filtrar_por_origen(self):
        while True:
            print(
                "IMPORTANTE: Deben ser solo LETRAS, ademas ambas iniciales deben empezar con MAYUSCULAS ej: Belgica o Costa Rica.")
            filtrar = input("Ingrese el pais de origen que desea filtrar de los jugadores: ")
            if not filtrar.isalpha() or not filtrar.istitle():
                continue
            try:
                with open("jugadores.json", "r") as jugadores_file:
                    jugadores = json.load(jugadores_file)
# esta primera (jugador_expresion) es una variable de iteracion que se utiliza para recorrer cada elemento de la lista jugadores.
                    filtrar_jugadores = [jugador_expresion for jugador_expresion in jugadores if jugador_expresion["origen"] == filtrar]
                    if jugadores:
                        print("Jugadores encontrados: ")
                        for jugador_expresion in filtrar_jugadores:
                            print(json.dumps(jugador_expresion, indent=4))
                        opcion = input("Desea realizar otra consulta? (SI/NO): ")
                        if opcion.lower() != 'si':
                            print("Volviendo al menu anterior...")
                            time.sleep(2)
                            break
                    else:
                        print("No se encontraron jugadores del origen especificido")

            except FileNotFoundError:
                print("No existe el archivo")
            except json.decoder.JSONDecodeError:
                print("El archivo jugadores.json no contiene datos legibles")

    def filtrar_por_reconocimientos(self):
        while True:
            print("IMPORTANTE: Deben ser solo NUMEROS, ej: 10, 20, 2")
            try:
                filtrar = int(input("Ingrese los reconocimientos que desea filtrar de los jugadores: "))
            except ValueError:
                print("Error: Debe ingresar un NUMERO entero")
                continue

            try:
                with open("jugadores.json", "r") as jugadores_file:
                    jugadores = json.load(jugadores_file)
                    # esta primera (jugador_expresion) es una variable de iteracion que se utiliza para recorrer cada elemento de la lista jugadores.
                    filtrar_jugadores = [jugador_expresion for jugador_expresion in jugadores if jugador_expresion["reconocimientos"] == filtrar]
                    if jugadores:
                        print("Jugadores encontrados: ")
                        for jugador_expresion in filtrar_jugadores:
                            print(json.dumps(jugador_expresion, indent=4))
                        opcion = input("Desea realizar otra consulta? (SI/NO): ")
                        if opcion.lower() != 'si':
                            print("Volviendo al menu anterior...")
                            time.sleep(2)
                            break
                    else:
                        print("No se encontraron jugadores con los reconocimientos especificidos")

            except FileNotFoundError:
                print("No existe el archivo")
            except json.decoder.JSONDecodeError:
                print("El archivo jugadores.json no contiene datos legibles")

    def visualizar_todos_jugadores(self):
        try:
            with open("jugadores.json", "r") as file:
                jugadores_datos = json.load(file)
                print(json.dumps(jugadores_datos, indent=4))
        except FileNotFoundError:
            print("El archivo 'jugadores.json' no se encontró.")
        except json.JSONDecodeError:
            print("El archivo 'jugadores.json' no contiene datos JSON válidos.")
        while True:
            opcion = input("Para volver al menu anterior digite (exit): ")
            if opcion.lower() == 'exit':
                print("Volviendo al menu.")
                time.sleep(2)
                return
            else:
                print("Por favor, digite (exit).")

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
                time.sleep(1)

#Gestion de jugadores Gestion de jugadores Gestion de jugadores Gestion de jugadores

    def insertar_nuevo_jugador(self):
        while True:
            # Solicitar al usuario que ingrese los datos del nuevo jugador
            nombre_jugador = input("Ingrese el nombre del jugador (Ej: Lionel Andres Messi) o (SALIR, regresar al menu de gestion): ")

            if nombre_jugador.lower() == "salir":
                return()

            if not nombre_jugador.replace(" ", "").isalpha() or not nombre_jugador.istitle():
                print("\nError: El nombre debe contener solo letras y comenzar con mayuscula Ej: Lionel Andres.")
                continue

            with open("jugadores.json", "r") as jugadores_file:
                jugadores_no_repetir_nombre = json.load(jugadores_file)

            nombre_existente = False
            for jugador in jugadores_no_repetir_nombre:
                if jugador.get("nombre") == nombre_jugador:
                    nombre_existente = True

            if nombre_existente:
                print("\nError: Este nombre ya esta en uso. Por favor, ingrese un nombre diferente.")
                continue

            while True:
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del jugador (Ej: 28 de octubre de 1991): ")

                # Definir el patron regex para validar la fecha de nacimiento
                patron_fecha = r"^\d{1,2} de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) de \d{4}$"

                # Verificar si la entrada coincide con el patron regex
                if re.match(patron_fecha, fecha_nacimiento.lower()):
                    break
                else:
                    print("Error: El formato de la fecha de nacimiento no es válido. Debe ser en el formato 'dd de mes de año'. Por ejemplo, '28 de octubre de 1991'.")

            origen = input("Ingrese el origen del jugador (Ej: Costa Rica): ")
            if not origen.replace(" ", "").isalpha() or not origen.istitle():
                print("\nError: El nombre debe contener solo letras y debe empezar con mayuscula.")
                continue

            genero = input("Ingrese el género del jugador (Masculino/Femenino): ")
            if not genero.isalpha():
                print("\nError: El genero debe contener solo letras")
            if not (genero == "Masculino" or genero == "Femenino"):
                print("\nError: Debe ser Masculino o Femenino")
                continue

            altura = input("Ingrese la altura del jugador (Ej: 1.82) (Min:1.0, Max:2.1 MTS): ")
            try:
                altura = float(altura)
                if altura < 1 or altura > 2.1:
                    print("\nError: Debe ser una altura entre 1.0 y 2.0")
                    continue
            except ValueError:
                print("\nError: La altura debe ser un número decimal y debe llever un(.)")
                continue

            peso = input("Ingrese el peso del jugador (Ej: 82.5kgs) (Min:50, Max:130 KGS: ")
            try:
                peso = float(peso)
                if peso < 50 or peso > 130:
                    print("\nError: Debe ser un peso entre 50 y 130kgs")
                    continue
            except ValueError:
                print("\nError: El peso debe ser un número decimal y debe llever un(.)")
                continue

            posicion_campo = input("Ingrese la posición en el campo del jugador (Ej: Delantero): ")
            if not posicion_campo.isalpha() and not posicion_campo.istitle():
                print("\nError: El campo debe ser en letras y las iniciales MAYUSCULAS ej: Delantero o Extremo Derecho.")
                continue

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

            while True:
                idx = input("Ingrese el ID del jugador (Ej: 30): ")
                if not idx.isdigit():
                    print("\nError: El ID debe ser un número entero.")
                    continue

                with open("estadistica_jugador.json", "r") as file:
                    jugadores_id_y_nombres = json.load(file)

                idx = int(idx)
                id_existente = False
                for jugador in jugadores_id_y_nombres:
                    if jugador.get("ID") == idx:
                        id_existente = True
                        break

                if id_existente:
                    print("\nError: Este ID ya está en uso. Por favor, ingrese un ID diferente.")
                else:
                    break  # El ID es valido y unico


            jugador = input("Ingrese el nombre del jugador nuevamente (Debe ser exactamente igual): ")
            if not jugador == nombre_jugador:
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
                "nombre": nombre_jugador,
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

        while True:
            with open("jugadores.json", "r") as nombre_file:
                ver_nombre = json.load(nombre_file)

            with open("estadistica_jugador.json", "r") as ID_file:
                ver_ID = json.load(ID_file)

            print("\nIMPORTANTE: El ID y el nombre del jugador deben ser EXACTOS...")
            preguntar_nombre = input("Ingrese el nombre del jugador que desea consultar informacion: ")
            preguntar_ID = input("Ingrese el ID del jugador que desea consultar informacion: ")

            if not preguntar_nombre.isalpha() or not preguntar_ID.isnumeric():
                print("\nError: Debe ingresar los datos correctos, en ID un NUMERO entero, en nombre LETRAS")
                continue

            jugador_existente = False
            for jugador in ver_nombre:
                if jugador["nombre"] == preguntar_nombre:
                    for IDx in ver_ID:
                        if IDx["ID"] == (preguntar_ID):
                            jugador_existente = True
# En vez de key y value puede ser cualquier parametro, para mas legibilidad asi, tambien podria ser (for nombre, informacion in jugador.items():
                            print("\nInformacion del jugador:")
                            for key, value in jugador.items():
                                print(f"{key}: {value}")
                            for key, value in IDx.items():
                                print(f"{key}: {value}")
                            repetir = input("Desea consultar la informacion de otro jugador? (SI/NO): ")
                            if repetir.lower() != "si":
                                print("\nVolviendo al gestor de jugadores...")
                                time.sleep(2)
                                return ()

            if not jugador_existente:
                print("\nNo se encontro el jugador que se especifico, intentelo de nuevo...")
                repetir = input("Desea consultar la informacion de otro jugador? (SI/NO): ")
                if repetir.lower() != "si":
                    print("\nVolviendo al gestor de jugadores...")
                    time.sleep(2)
                    return ()

    def modificar_datos_jugador(self):
        while True:
            with open("jugadores.json", "r") as informacion_jugadores_file:
                informacion_jugadores = json.load(informacion_jugadores_file)

            with open("estadistica_jugador.json", "r") as estadisticas_jugadores_file:
                estadisticas_jugadores = json.load(estadisticas_jugadores_file)

            print("\nIMPORTANTE: El ID y el nombre del jugador deben ser EXACTOS...")
            pedir_nombre_jugador = input("Ingrese el nombre del jugador que desea modificar: ")
            pedir_id_jugador = input("Ingrese el ID del jugador que desea modificar: ")

            if not pedir_nombre_jugador.isalpha() or not pedir_id_jugador.isnumeric():
                print("El nombre del jugador debe ser en LETRAS y el ID del jugador en NUMEROS...")
                continue

            nombre_existente = False
            for nombre in informacion_jugadores:
                if nombre["nombre"] == pedir_nombre_jugador:
                    for idx in estadisticas_jugadores:
                        if idx["ID"] == pedir_id_jugador:
                            nombre_existente = True

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