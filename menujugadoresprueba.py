import json
import time
import re

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

    def estadisticas_jugadores(self):
        while True:
            print("\nEstadisticas de jugadores: ")
            print("1-Ver las estadisticas de un jugador")
            print("2-Comparar las estadisticas de dos jugadores")
            print("3-Volver al menu principal")

            opcion = input("Seleccione una opcion y digitela: ")

            if opcion == '1':
                self.ver_estadisticas_jugador()

            elif opcion == '2':
                self.comparar_estadisticas()

            elif opcion == '3':
                print("Volviendo al menu principal")
                time.sleep(2)
                return()
            else:
                print("Opcion invalida, intentelo de nuevo.")

    def consultas_avanzadas(self):
        while True:
            print("\n-----------------------------------------------Consultas Avanzadas-----------------------------------------------")
            print("1-Mostrar la cantidad de jugadores de acuerdo al origen")
            print("2-Mostrar todos los jugadores que se encuentren en un rango de edad")
            print("3-Mostrar la cantidad de jugadores de acuerdo con la altura que tienen y con referencia al genero de cada uno")
            print("4-Mostrar los jugadores de Club específico")
            print("5-Mostrar la cantidad de jugadores de acuerdo con la posición en el campo que posee, considerando unicamente los de genero femenino")
            print("6-Mostrar el top 10 de los jugadores con mayor altura y con mejor agilidad, la informacion que se muestra es el nombre, genero, origen, altura y agilidad")
            print("7-Mostrar la cantidad de jugadores cuya velocidad esté en un rango específico")
            print("8-Determinar el promedio de control de balón para jugadores en una posición específica")
            print("9-Volver al Menu Principal")
            print("--------------------------------------------------------------------------------------------------------------------")

            opcion = input("Seleccione una opcion y digitela: ")

            if opcion == "1":
                self.Mostrar_cantidad_jugadores_mismo_origen()
            if opcion == "2":
                self.Mostrar_todos_los_jugadores_que_se_encuentren_en_un_rango_de_edad()
            if opcion == "3":
                self.Mostrar_cantidad_jugadores_con_misma_altura_y_tienen_referencia_al_género_de_cada_uno()
            if opcion == "4":
                self.Mostrar_los_jugadores_de_Club_específico()
            if opcion == "5":
                self.Mostrar_cantidad_jugadores_acuerdo_con_la_posición_en_el_campo_considerando_unicamente_los_de_género_femenino()
            if opcion == "6":
                self.Mostrar_top_diez_jugadores_mayor_altura_con_mejor_agilidad_la_información_muestra_nombre_genero_origen_altura_agilidad()
            if opcion == "7":
                self.Mostrar_cantidad_jugadores_cuya_velocidad_este_en_un_rango_específico()
            if opcion == "8":
                self.Determinar_promedio_control_balon_para_jugadores_en_una_posición_específica()
            if opcion == "9":
                print("Volviendo al menu principal...")
                time.sleep(2)
                return()

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

#visualizar_lista_jugadores #visualizar_lista_jugadores #visualizar_lista_jugadores #visualizar_lista_jugadores #visualizar_lista_jugadores
    def filtrar_por_posicion_campo(self):
        while True:
            print("IMPORTANTE: Deben ser solo LETRAS, ademas ambas iniciales deben empezar con MAYUSCULAS ej: Delantero o Extremo Derecho.")
            filtrar = input("Ingrese la posicion que desea filtrar de los jugadores,(SI desea volver al menu anterior digite (EXIT): ")
            if filtrar.lower() == "exit":
                return()
            if not filtrar.replace(" ","").isalpha() or not filtrar.istitle():
                continue
            try:
                with open("jugadores.json", "r") as jugadores_file:
                    jugadores = json.load(jugadores_file)
                    # esta primera (jugador_expresion) es una variable de iteracion que se utiliza para recorrer cada elemento de la lista jugadores.
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
            filtrar = input("Ingrese el pais de origen que desea filtrar de los jugadores,(SI desea volver al menu anterior digite (EXIT):: ")
            if filtrar.lower() == "exit":
                return()
            if not filtrar.replace(" ","").isalpha() or not filtrar.istitle():
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
            print("IMPORTANTE: Deben ser solo NUMEROS, (Ej: 10, 20, 2)")
            try:
                filtrar = int(input("Ingrese los reconocimientos que desea filtrar de los jugadores(SI desea volver al menu anterior digite (000):: "))
                if filtrar == 000:
                    return()
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

#Visualizar estadisticas jugadores #Visualizar estadisticas jugadores #Visualizar estadisticas jugadores #Visualizar estadisticas jugadores #Visualizar estadisticas jugadores

    def ver_estadisticas_jugador(self):
        while True:
            jugador_encontrado = False
            while True:
                nombre_jugador = input("Ingrese el nombre de jugador cuyas estadisticas desea ver: ")
                if not nombre_jugador.replace(" ", "").isalpha() or not nombre_jugador.istitle():
                    print("Error: El nombre de jugador debe iniciar con MAYUSCULA y solo se permiten letras.")
                    continue
                else:
                    break

            with open("estadistica_jugador.json", "r") as file:
                estadisticas = json.load(file)

            for nombre in estadisticas:
                if nombre["Jugador"] == nombre_jugador:
                    jugador_encontrado = True
                    print("\nEstadisticas de Jugador: ")
                    print(json.dumps(nombre, indent=4))

                    opcion = input("Desea consultar a otro jugador?(SI/NO): ")
                    if opcion.lower() != "si":
                        print("Volviendo al menu anterior")
                        time.sleep(2)
                        return ()
                    else:
                        break

            if not jugador_encontrado:
                print("El jugador no fue encontrado o no existe.")
                opcion = input("Desea consultar a otro jugador?(SI/NO): ")
                if opcion.lower() != "si":
                    print("Volviendo al menu anterior")
                    time.sleep(2)
                    return ()

    def comparar_estadisticas(self):
        while True:
            while True:
                nombre1 = input("Ingrese el nombre del primer jugador, si desea volver al menu anterior digite (EXIT): ")

                if nombre1.lower() == "salir":
                    print("Volviendo al menu anterior")
                    time.sleep(2)
                    return()

                if not nombre1.replace(" ", "").isalpha() or not nombre1.istitle():
                    print("Error: El nombre de jugador debe iniciar con MAYUSCULA y solo se permiten letras.")
                    continue
                else:
                    break

            while True:
                nombre2 = input("Ingrese el nombre del segundo jugador: ")
                if not nombre2.replace(" ", "").isalpha() or not nombre2.istitle():
                    print("Error: El nombre de jugador debe iniciar con MAYUSCULA y solo se permiten letras.")
                    continue
                else:
                    break

            with open("jugadores.json", "r") as file:
                estadistica = json.load(file)

            jugador1 = None
            jugador2 = None

            for jugador in estadistica:
                if jugador["nombre"] == nombre1:
                    jugador1 = jugador
                elif jugador["nombre"] == nombre2:
                    jugador2 = jugador


            if jugador1 is None or jugador2 is None:
                print("Uno o ambos jugadores no se encontraron, intente de nuevo")
                opcion = input("Desea hacer otra comparacion?(SI/NO): ")
                if opcion.lower() != "si":
                    print("Volviendo al menu anterior")
                    time.sleep(2)
                    return ()

                continue

            if jugador1["posicion_campo"] != jugador2["posicion_campo"]:
                print("Los jugadores no poseen la misma posicion de campo y no son comparables")
                opcion = input("Desea hacer otra comparacion?(SI/NO): ")
                if opcion.lower() != "si":
                    print("Volviendo al menu anterior")
                    time.sleep(2)
                    return()

                continue

            print("\nEstadisticas del primer jugador: ")
            print(json.dumps(jugador1, indent=4))
            print("\nEstadisticas del segundo jugador: ")
            print(json.dumps(jugador2, indent=4))

            opcion = input("Desea hacer otra comparacion?(SI/NO): ")
            if opcion.lower() != "si":
                print("Volviendo al menu anterior")
                time.sleep(2)
                return ()

            continue

#Gestion de jugadores Gestion de jugadores Gestion de jugadores Gestion de jugadores

    def insertar_nuevo_jugador(self):
        while True:
            # Solicitar al usuario que ingrese los datos del nuevo jugador
            nombre_jugador = input("Ingrese el nombre del jugador que desea ingresar (Ej: Lionel Andres Messi) o (SALIR, regresar al menu de gestion): ")

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

            while True:
                origen = input("Ingrese el origen del jugador (Ej: Costa Rica): ")
                if not origen.replace(" ", "").isalpha() or not origen.istitle():
                    print("\nError: El nombre debe contener solo letras y debe empezar con mayuscula.")
                    continue
                else:
                    break

            while True:
                genero = input("Ingrese el género del jugador (Masculino/Femenino/Otro): ")
                if not genero.isalpha():
                    print("\nError: El genero debe contener solo letras")
                if not (genero == "Masculino" or genero == "Femenino" or genero == "Otro"):
                    print("\nError: Debe ser Masculino o Femenino")
                    continue
                else:
                    break

            while True:
                try:
                    altura = float(input("Ingrese la altura del jugador (Ej: 1.82) (Min:1.0, Max:2.1 MTS): "))
                    if altura < 1.0 or altura > 2.1:
                        print("\nError: Debe ser una altura entre 1.0 y 2.1 MTS")
                        continue
                    else:
                        break
                except ValueError:
                    print("Error: Ingrese solo NUMEROS decimales en el formato adecuado (Ej: 1.82)")
                    continue

            while True:
                try:
                    peso = float(input("Ingrese el peso del jugador (Ej: 82.5kgs) (Min:50, Max:130 KGS): "))
                    if peso < 50 or peso > 130:
                        print("\nError: Debe ser un peso entre 50 y 130kgs")
                        continue
                    else:
                        break
                except ValueError:
                    print("Error: Ingrese solo NUMEROS decimales o enteros en el formato adecuado (Ej: 82.5 o 90 KGS)")
                    continue

            posicion_campo = input("Ingrese la posición en el campo del jugador (Ej: Delantero): ")
            if not posicion_campo.isalpha() and not posicion_campo.istitle():
                print("\nError: El campo debe ser en letras y las iniciales MAYUSCULAS ej: Delantero o Extremo Derecho.")
                continue

            club_militante = input("Ingrese el club militante del jugador (Ej: Inter Miami): ")
            if club_militante.replace(" ", "").isalpha() and club_militante.istitle():
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

            print("\nADVERTENCIA: A partir de aqui si digita algo que no se le indica VOLVERA al INICIO...\n")
            jugador = input("Ingrese el nombre del jugador nuevamente (Debe ser exactamente igual): ")
            if not jugador == nombre_jugador:
                print("\nError: El nombre del jugador debe de ser el mismo")
                continue

            aceleracion = input("Ingrese la aceleracion del jugador (Ej: 42-99): ")
            try:
                aceleracion = int(aceleracion)
                if aceleracion < 42 or aceleracion > 99:
                    print("\nError: El valor no debe ser menor a 42 y mayor a 99")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            pases_cortos = input("Ingrese la estadistica de pases cortos del jugador(Ej: 42-99): ")
            pases_cortos = int(pases_cortos)
            try:
                if pases_cortos < 42 or pases_cortos > 99:
                    print("\nError: El valor no debe ser menor a 42 y mayor a 99")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            potencia_tiro = input("Ingrese la potencia de tiro del jugador (Ej: 42-99): ")
            potencia_tiro = int(potencia_tiro)
            try:
                if potencia_tiro < 42 or potencia_tiro > 100:
                    print("\nError: El valor no debe ser menor a 42 y mayor a 99")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            pases_largos = input("Ingrese la estadistica de pases largos del jugador(Ej: 42-99): ")
            pases_largos = int(pases_largos)
            try:
                if pases_largos < 42 or pases_largos > 99:
                    print("\nError: El valor no debe ser menor a 42 y mayor a 99")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            velocidad = input("Ingrese la velocidad del jugador(Ej: 42-99): ")
            velocidad = int(velocidad)
            try:
                if velocidad < 42 or velocidad > 99:
                    print("\nError: El valor no debe ser menor a 42 y mayor a 99")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            agilidad = input("Ingrese la agilidad del jugador(Ej: 42-99): ")
            agilidad = int(agilidad)
            try:
                if agilidad < 42 or agilidad > 99:
                    print("\nError: El valor no debe ser menor a 42 y mayor a 99")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            resistencia = input("Ingrese la resistencia del jugador(Ej: 42-99): ")
            resistencia = int(resistencia)
            try:
                if resistencia < 42 or resistencia > 99:
                    print("\nError: El valor no debe ser menor a 0 y mayor a 100")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            salto = input("Ingrese el salto del jugador(Ej: 42-99): ")
            salto = int(salto)
            try:
                if salto < 42 or salto > 99:
                    print("\nError: El valor no debe ser menor a 42 y mayor a 99")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue

            regates = input("Ingrese la estadistica de regate del jugador(Ej: 42-99): ")
            regates = int(regates)
            try:
                if regates < 42 or regates > 99:
                    print("\nError: El valor no debe ser menor a 42 y mayor a 99")
                    continue
            except ValueError:
                    print("\nError: Debe ingresar un número entero.")
                    continue
            control_balon = input("Ingrese la estadistica de control de balon del jugador(Ej: 42-99): ")
            control_balon = int(control_balon)
            try:
                if control_balon < 42 or control_balon > 99:
                    print("\nError: El valor no debe ser menor a 42 y mayor a 99")
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

            print("\nNuevo jugador agregado con éxito.")
            time.sleep(2)
            return()

    def leer_informacion_jugador(self):

        while True:
            with open("jugadores.json", "r") as nombre_file:
                ver_nombre = json.load(nombre_file)

            with open("estadistica_jugador.json", "r") as ID_file:
                ver_ID = json.load(ID_file)

            print("\nIMPORTANTE: El NOMBRE del jugador DEBE ser EXACTO (Ej: Lionel Andres Messi)...")
            preguntar_nombre = input("Ingrese el nombre del jugador que desea consultar informacion: ")

            if not preguntar_nombre.replace(" ","").isalpha():
                print("\nError: Debe ingresar los datos correctos, en ID un NUMERO entero, en nombre LETRAS")
                continue

            jugador_existente = False
            for jugador in ver_nombre:
                if jugador["nombre"] == preguntar_nombre:
                    for jugadorr in ver_ID:
                        if jugadorr["Jugador"] == preguntar_nombre:
                            jugador_existente = True
# En vez de key y value puede ser cualquier parametro, para mas legibilidad asi, tambien podria ser (for nombre, informacion in jugador.items():
                            print("\nInformacion del jugador:")
                            for key, value in jugador.items():
                                print(f"{key}: {value}")
                            for key, value in jugadorr.items():
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

            print("\nIMPORTANTE: El NOMBRE del jugador DEBE ser EXACTO (Ej: Lionel Andres Messi)...")

            pedir_nombre_jugador = input("Ingrese el nombre del jugador que desea modificar(SI desea volver al menu anterior digite EXIT): ")
            if pedir_nombre_jugador.lower() == "exit":
                print("Volviendo al menu anterior...")
                time.sleep(2)
                return ()

            if not pedir_nombre_jugador.replace(" ","").isalpha():
                print("El nombre del jugador debe ser en LETRAS y el ID del jugador en NUMEROS...")
                continue

            nombre_existente = False
            for nombre in informacion_jugadores:
                if nombre["nombre"] == pedir_nombre_jugador:
                    for jugadorr in estadisticas_jugadores:
                        if jugadorr["Jugador"] == pedir_nombre_jugador:
                            nombre_existente = True
                            print("\nInformacion basica del jugador:")
                            print(json.dumps(nombre, indent=4))
                            print("\nInformacion estadistica del jugador:")
                            print(json.dumps(jugadorr, indent=4))
                            while True:
                                nuevo_nombre = input("Ingrese el nuevo nombre, si no desea cambiar este dato digite el mismo dato: ")
                                if not nuevo_nombre.replace(" ", "").isalpha() or not nuevo_nombre.istitle():
                                    print("\nError: El nombre debe contener solo letras y debe empezar con mayuscula.")
                                    continue
                                else:
                                    break

                            while True:
                                nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento, si no desea cambiar este dato digite el mismo dato: ")
                                # Definir el patron regex para validar la fecha de nacimiento
                                patron_fecha = r"^\d{1,2} de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) de \d{4}$"

                                # Verificar si la entrada coincide con el patron regex
                                if re.match(patron_fecha, nueva_fecha_nacimiento.lower()):
                                    break
                                else:
                                    print("Error: El formato de la fecha de nacimiento no es válido. Debe ser en el formato 'dd de mes de año'. Por ejemplo, '28 de octubre de 1991'.")

                            while True:
                                nuevo_genero = input("Ingrese el nuevo genero, si no desea cambiar este dato digite el mismo dato(Masculino/Femenino/Otro): ")
                                if nuevo_genero in ["Masculino", "Femenino", "Otro"]:
                                    break
                                else:
                                    print("Debe ser exactamente (Masculino/Femenino/Otro), respetando la mayuscula inicial")

                            while True:
                                try:
                                    nueva_altura = float(input("Ingrese la nueva altura, si no desea cambiar este dato digite el mismo dato: "))
                                    if nueva_altura < 1.0 or nueva_altura > 2.1:
                                        print("Error: Ingrese solo NUMEROS, ademas debe ser decimal, con un limite (Min:1.0, Max:2.1 MTS), (Ej: 1.82) : ")
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print("Error: Ingrese solo NUMEROS decimales en el formato adecuado (Ej: 1.82)")
                                    continue

                            while True:
                                try:
                                    nuevo_peso = float(input("Ingrese el nuevo peso, si no desea cambiar este dato digite el mismo dato: "))
                                    if nuevo_peso < 50 or nuevo_peso > 130:
                                        print("Error: Ingrese solo NUMEROS, ademas debe ser decimal, con un limite (Min:50, Max:130 KGS), (Ej: 72) : ")
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print("Error: Ingrese solo números decimales en el formato adecuado (Ej: 72, 72.5 KGS)")
                                    continue

                            while True:
                                nueva_posicion_campo = input("Ingrese la nueva posicion de campo, si no desea cambiar este dato digite el mismo dato: ")
                                if not nueva_posicion_campo.replace(" ", "").isalpha or not nueva_posicion_campo.istitle():
                                    print("Error: Debe empezar con MAYUSCULA y deben ser solo letras ")
                                    continue
                                else:
                                    break

                            while True:
                                nuevo_club_militante = input("Ingrese el nuevo club militante, si no desea cambiar este dato digite el mismo dato: ")
                                if not nuevo_club_militante.replace(" ", "").isalpha() or not nuevo_club_militante.istitle():
                                    print("Error: Debe empezar con MAYUSCULA y deben ser solo letras ")
                                    continue
                                else:
                                    break

                            while True:
                                nuevo_reconocimiento = input("Ingrese el nuevo(s) reconocimientos, si no desea cambiar este dato digite el mismo dato: ")
                                if not nuevo_reconocimiento.isnumeric():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                else:
                                    nuevo_reconocimiento = int(nuevo_reconocimiento)
                                    break

                            nombre["nombre"] = nuevo_nombre
                            nombre["fecha_nacimiento"] = nueva_fecha_nacimiento
                            nombre["genero"] = nuevo_genero
                            nombre["altura"] = nueva_altura
                            nombre["peso"] = nuevo_peso
                            nombre["posicion_campo"] = nueva_posicion_campo
                            nombre["club_militante"] = nuevo_club_militante
                            nombre["reconocimientos"] = nuevo_reconocimiento

                            with open("jugadores.json", "w") as informacion_jugadores_file:
                                json.dump(informacion_jugadores, informacion_jugadores_file, indent=4)

                            print("Los cambios se han aplicado correctamente...")
                            while True:
                                opcion_si_no = input("Desea tambien modificar las estadisticas del jugador?(SI/NO): ")
                                if opcion_si_no.lower() == "si":
                                    break
                                elif opcion_si_no.lower() == "no":
                                    print("Volviendo al menu anterior...")
                                    time.sleep(2)
                                    return()
                                else:
                                    print("Digite (SI o NO)")

                            while True:
                                nueva_aceleracion = input("Ingrese la nueva estadistica de aceleracion, si no desea cambiar este dato digite el mismo dato: ")
                                if not nueva_aceleracion.isnumeric() or nueva_aceleracion.isalpha():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                nueva_aceleracion = int(nueva_aceleracion)
                                if nueva_aceleracion < 42 or nueva_aceleracion > 99:
                                    print("\nError: El valor no DEBE ser MENOR a 42 y MAYOR a 99")
                                    continue
                                else:
                                    break

                            while True:
                                nuevo_pases_cortos = input("Ingrese la nueva estadistica de pases cortos, si no desea cambiar este dato digite el mismo dato: ")
                                if not nuevo_pases_cortos.isnumeric() or nuevo_pases_cortos.isalpha():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                nuevo_pases_cortos = int(nuevo_pases_cortos)
                                if nuevo_pases_cortos < 42 or nuevo_pases_cortos > 99:
                                    print("\nError: El valor no DEBE ser MENOR a 42 y MAYOR a 99")
                                    continue
                                else:
                                    break

                            while True:
                                nueva_potencia_tiro = input("Ingrese la nueva estadistica de potencia de tiro, si no desea cambiar este dato digite el mismo dato: ")
                                if not nueva_potencia_tiro.isnumeric() or nueva_potencia_tiro.isalpha():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                nueva_potencia_tiro = int(nueva_potencia_tiro)
                                if nueva_potencia_tiro < 42 or nueva_potencia_tiro > 99:
                                    print("\nError: El valor no DEBE ser MENOR a 42 y MAYOR a 99")
                                    continue
                                else:
                                    break

                            while True:
                                nuevo_pases_largos = input("Ingrese la nueva estadistica de pases largos, si no desea cambiar este dato digite el mismo dato: ")
                                if not nuevo_pases_largos.isnumeric() or nuevo_pases_largos.isalpha():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                nuevo_pases_largos = int(nuevo_pases_largos)
                                if nuevo_pases_largos < 42 or nuevo_pases_largos > 99:
                                    print("\nError: El valor no DEBE ser MENOR a 42 y MAYOR a 99")
                                    continue
                                else:
                                    break

                            while True:
                                nueva_velocidad = input("Ingrese la nueva estadistica de velocidad, si no desea cambiar este dato digite el mismo dato: ")
                                if not nueva_velocidad.isnumeric() or nueva_velocidad.isalpha():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                nueva_velocidad = int(nueva_velocidad)
                                if nueva_velocidad < 42 or nueva_velocidad > 99:
                                    print("\nError: El valor no DEBE ser MENOR a 42 y MAYOR a 99")
                                    continue
                                else:
                                    break

                            while True:
                                nueva_agilidad = input("Ingrese la nueva estadistica de agilidad, si no desea cambiar este dato digite el mismo dato: ")
                                if not nueva_velocidad.isnumeric() or nueva_velocidad.isalpha():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                nueva_agilidad = int(nueva_agilidad)
                                if nueva_agilidad < 42 or nueva_agilidad > 99:
                                    print("\nError: El valor no DEBE ser MENOR a 42 y MAYOR a 99")
                                    continue
                                else:
                                    break

                            while True:
                                nueva_resistencia = input("Ingrese la nueva estadistica de resistencia, si no desea cambiar este dato digite el mismo dato: ")
                                if not nueva_resistencia.isnumeric() or nueva_resistencia.isalpha():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                nueva_resistencia = int(nueva_resistencia)
                                if nueva_resistencia < 42 or nueva_resistencia > 99:
                                    print("\nError: El valor no DEBE ser MENOR a 42 y MAYOR a 99")
                                    continue
                                else:
                                    break

                            while True:
                                nuevo_salto = input("Ingrese la nueva estadistica de salto, si no desea cambiar este dato digite el mismo dato: ")
                                if not nuevo_salto.isnumeric() or nuevo_salto.isalpha():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                nuevo_salto = int(nuevo_salto)
                                if nuevo_salto < 42 or nuevo_salto > 99:
                                    print("\nError: El valor no DEBE ser MENOR a 42 y MAYOR a 99")
                                    continue
                                else:
                                    break

                            while True:
                                nuevo_regate = input("Ingrese la nueva estadistica de regate, si no desea cambiar este dato digite el mismo dato: ")
                                if not nuevo_regate.isnumeric() or nuevo_regate.isalpha():
                                    print("Error: Debe ser NUMEROS enteros")
                                    continue
                                nuevo_regate = int(nuevo_regate)
                                if nuevo_regate < 42 or nuevo_regate > 99:
                                    print("\nError: El valor no DEBE ser MENOR a 42 y MAYOR a 99")
                                    continue
                                else:
                                    break

                            jugadorr["Jugador"] = nuevo_nombre
                            jugadorr["Aceleracion"] = nueva_aceleracion
                            jugadorr["Pases cortos"] = nuevo_pases_cortos
                            jugadorr["Potencia de tiro"] = nueva_potencia_tiro
                            jugadorr["Pases largos"] = nuevo_pases_largos
                            jugadorr["Velocidad"] = nueva_velocidad
                            jugadorr["Agilidad"] = nueva_agilidad
                            jugadorr["Resistencia"] = nueva_resistencia
                            jugadorr["Salto"] = nuevo_salto
                            jugadorr["Regates"] = nuevo_regate

                            with open("estadistica_jugador.json", "w") as estadisticas_jugadores_file:
                                json.dump(estadisticas_jugadores, estadisticas_jugadores_file, indent=4)

                            print("Datos del jugador actualizados correctamente")
                            consultar = input("Desea modificar otro jugador?(SI/NO)")
                            if consultar.lower() != "si":
                                print("Volviendo al menu anterior...")
                                time.sleep(2)
                                return()

            if not nombre_existente:
                print("No se encontro al jugador con el ID y nombre especificados...")

    def eliminar_jugador(self):
        while True:
            nombre_jugador = input("Ingrese el nombre del jugador que desea eliminar, si desea volver al menu anterior ingrese (EXIT): ")

            if nombre_jugador.lower() == "exit":
                print("Volviendo al menu anterior")
                time.sleep(2)
                return()

            if not nombre_jugador.replace(" ", "").isalpha() or not nombre_jugador.istitle():
                print("Error: El nombre del jugador debe empezar con MAYUSCULA y deben ser solo letras")
                continue

            with open("jugadores.json", "r") as jugadores_file:
                jugadores = json.load(jugadores_file)

            jugadores_actualizados = [jugador for jugador in jugadores if jugador["nombre"] != nombre_jugador]

            if len(jugadores_actualizados) == len(jugadores):
                print(f"El jugador {nombre_jugador} no se encontro en la lista")
                continue

            with open("jugadores.json", "w") as jugadores_file:
                json.dump(jugadores_actualizados, jugadores_file, indent=4)

            with open("estadistica_jugador.json", "r") as estadistica_jugador_file:
                estadistica_jugador = json.load(estadistica_jugador_file)

            estadisticas_actualizadas = [estadistica for estadistica in estadistica_jugador if estadistica["Jugador"] != nombre_jugador]

            if len(estadisticas_actualizadas) == len(estadistica_jugador):
                print(f"El jugador {nombre_jugador} no se encontro en la lista")
                continue

            with open("estadistica_jugador.json", "w") as estadistica_jugador_file:
                json.dump(estadisticas_actualizadas, estadistica_jugador_file, indent=4)

            print(f"El jugador {nombre_jugador} se ha eliminado con exito")

            consultar = input("Desea modificar otro jugador?(SI/NO)")
            if consultar.lower() != "si":
                print("Volviendo al menu anterior...")
                time.sleep(2)
                return ()

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