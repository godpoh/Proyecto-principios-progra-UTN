import json
import time
import re

class Menu:
    def __init__(self):
        self.main_options = {
            '1': self.player_managment,
            '2': self.view_player_list,
            '3': self.players_statistics,
            '4': self.advanced_queries,
            '5': self.exit
        }

# Menu principal Menu principal Menu principal Menu principal Menu principal Menu principal

    def show_main_menu(self):
        print("\n------------Menu Principal------------")
        print("1-Gestion de Jugadores")
        print("2-Visualizar lista de jugadores")
        print("3-Estadísticas de Jugadores")
        print("4-Consultas avanzadas")
        print("5-Salir del sistema.")
        print("--------------------------------------")

    def player_managment(self):
        while True:
            print("\n------------Gestion de Jugadores------------")
            print("1-Insertar un nuevo jugador")
            print("2-Leer informacion de un jugador")
            print("3-Modificar datos de un jugador")
            print("4-Eliminar un jugador de la base de datos")
            print("5-Regresar al menu principal")
            print("--------------------------------------------")
            option = input("Ingrese el digito de la opcion(1-5): ")
            if option == '1':
                self.insert_new_player()
            elif option == '2':
                self.read_player_information()
            elif option == '3':
                self.modify_player_data()
            elif option == '4':
                self.remove_player()
            elif option == '5':
                print("Volviendo al menu principal")
                time.sleep(2)
                return
            else:
                print("Valor no valido, vuelva a intentarlo")

    def view_player_list(self):
        while True:
            print("\nSeleccione un filtro para visualizar la lista de jugadores")
            print("1-Por posicion de campo")
            print("2-Por origen(PAIS)")
            print("3-Por reconocimientos(BALONES DE ORO, ETC)")
            print("4-Regresar al Menu Principal")
            print("----------------------------------------------------------")

            option = input("Ingrese el numero de la opcion deseada: ")
            if option == '1':
                self.filter_by_field_position()
            elif option == '2':
                self.filter_by_origen()
            elif option == '3':
                self.filter_by_recognitions()
            elif option == '4':
                print("Volviendo al menu principal")
                time.sleep(2)
                return
            else:
                print("Opcion invalida, porfavor seleccione una opcion valida.")

    def players_statistics(self):
        while True:
            print("\nEstadisticas de jugadores: ")
            print("1-Ver las estadisticas de un jugador")
            print("2-Comparar las estadisticas de dos jugadores")
            print("3-Volver al menu principal")

            option = input("Seleccione una opcion y digitela: ")
            if option == '1':
                self.view_player_statistics()
            elif option == '2':
                self.compare_statistics()
            elif option == '3':
                print("Volviendo al menu principal")
                time.sleep(2)
                return
            else:
                print("Opcion invalida, intentelo de nuevo.")

    def advanced_queries(self):
        while True:
            print("\n-----------------------------------------------Consultas Avanzadas-----------------------------------------------")
            print("1-Mostrar la cantidad de jugadores de acuerdo al origen")
            print("2-Mostrar todos los jugadores que se encuentren en un rango de edad")
            print("3-Mostrar la cantidad de jugadores de acuerdo con la altura que tienen y con referencia al genero de cada uno")
            print("4-Mostrar los jugadores de Club específico")
            print("5-Mostrar la cantidad de jugadores de acuerdo con la posición en el campo que posee, considerando UNICAMENTE los de genero femenino")
            print("6-Mostrar el top 10 de los jugadores con mayor altura y con mejor agilidad, la informacion que se muestra es el nombre, genero, origen, altura y agilidad")
            print("7-Mostrar la cantidad de jugadores cuya velocidad esté en un rango específico")
            print("8-Determinar el promedio de control de balón para jugadores en una posición específica")
            print("9-Volver al Menu Principal")
            print("--------------------------------------------------------------------------------------------------------------------")

            option = input("Seleccione una opcion y digitela: ")
            if option == "1":
                self.show_number_player_same_origen()
            if option == "2":
                self.show_all_players_in_an_age_range()
            if option == "3":
                self.show_number_players_with_same_height_and_reference_to_gender_each_one()
            if option == "4":
                self.show_all_players_in_a_specific_club()
            if option == "5":
                self.show_number_of_players_accordance_position_on_field_considering_only_gender_female()
            if option == "6":
                self.show_top_ten_players_highest_with_best_agility_information_sample_name_gender_origin_height_agility()
            if option == "7":
                self.show_number_players_whose_speed_is_in_specific_range()
            if option == "8":
                self.determinate_average_ball_control_for_players_in_a_specific_position()
            if option == "9":
                print("Volviendo al menu principal...")
                time.sleep(2)
                return

    def exit(self):
        print("Saliendo del sistema.")
        exit()

    def main(self):
        while True:
            self.show_main_menu()
            option = input("Seleccione una opción: ")
            accion = self.main_options.get(option)
            if accion:
                accion()
            else:
                print("\nError: Opción no válida. Por favor, seleccione una opción válida.\n")
                time.sleep(1)

    def back_to_menu(self):
        print("IMPORTANTE: Si se digita algo diferente de 'SI' se tomara como un 'NO'")
        option = input("Desea realizar otra accion? (SI/NO): ")
        if option.lower() != 'si':
            print("Volviendo al menu anterior...")
            time.sleep(2)
            return False
        return True

    def validate_float_input(prompt, minValue, maxValue):
        while True:
            user_input = input(prompt)
            try:
                user_input = float(user_input)
                if minValue <= user_input <= maxValue:
                    return user_input
                else:
                    print(f"El valor debe de estar entre {minValue} y {maxValue}")
            except ValueError:
                print("Error: Debe ingresar un numero float")

    def validate_int_input(prompt, minValue, maxValue):
        while True:
            user_input = input(prompt)
            try:
                user_input = int(user_input)
                if minValue <= user_input <= maxValue:
                    return user_input
                else:
                    print(f"El valor debe de estar entre {minValue} y {maxValue}")
            except ValueError:
                print("Error: Debe ingresar un numero entero")

    def validate_string_input(prompt):
        while True:
            input_string = input(prompt)
            if not input_string.replace(" ", "").isalpha() or not input_string.istitle():
                print("Error: Deben ser solo LETRAS, ademas ambas iniciales deben empezar con MAYUSCULAS")
                continue
            return input_string

    def load_players_json(self):
        try:
            with open("players_data.json.json", "r") as players_file:
                return json.load(players_file)
        except FileNotFoundError:
            print("El archivo players_data.json.json no se ha encontrado")
            return None
        except json.decoder.JSONDecodeError:
            print("El archivo players_data.json.json no contiene datos legibles")
            return None

    def get_player_statistics(self, player_found):
        player_statistics = {
            "acceleration": player_found["acceleration"],
            "short_passes": player_found["short_passes"],
            "power_of_shot": player_found["power_of_shot"],
            "long_passes": player_found["long_passes"],
            "speed": player_found["speed"],
            "agility": player_found["agility"],
            "resistance": player_found["resistance"],
            "jump": player_found["jump"],
            "dribbling": player_found["dribbling"],
            "ball_control": player_found["ball_control"]
        }
        return player_statistics


#visualizar_lista_jugadores #visualizar_lista_jugadores #visualizar_lista_jugadores #visualizar_lista_jugadores #visualizar_lista_jugadores
    def filter_by_field_position(self):
        while True:
            print("IMPORTANTE: Deben ser solo LETRAS, ademas ambas iniciales deben empezar con MAYUSCULAS ej: Delantero o Extremo Derecho.")
            position_filter = Menu.validate_string_input("Ingrese la posicion que desea filtrar de los jugadores: ")
            try:
                players = self.load_players_json()
#esta primera(jugador_expresion)es una variable de iteracion que se utiliza para recorrer cada elemento de la lista jugadores.
                if players:
                    filter_players = [player_expression for player_expression in players["players"] if player_expression["position_in_field"] == position_filter]

                    if players:
                        print("Jugadores encontrados: ")
                        for player_expression in filter_players:
                            print(json.dumps(player_expression, indent=4))
                    else:
                        print("No se encontraron jugadores de la posicion especificida")
                else:
                    print("No se encontraron datos de jugadores en el archivo")

                if not self.back_to_menu():
                    break
            except FileNotFoundError:
                print("No existe el archivo")
                break
    def filter_by_origen(self):
        while True:
            print("IMPORTANTE: Deben ser solo LETRAS, ademas ambas iniciales deben empezar con MAYUSCULAS ej: Belgica o Costa Rica.")
            filter = Menu.validate_string_input("Ingrese el pais de origen que desea filtrar de los jugadores: ")
            try:
                if not self.load_players_json():
                    break
                players = self.load_players_json()
# esta primera (jugador_expresion) es una variable de iteracion que se utiliza para recorrer cada elemento de la lista jugadores.
                filter_players = [player_expression for player_expression in players["players"] if player_expression["origin"] == filter]
                if players:
                    print("Jugadores encontrados: ")
                    for player_expression in filter_players:
                        print(json.dumps(player_expression, indent=4))
                    if not self.back_to_menu():
                        break
                else:
                    print("No se encontraron jugadores del origen especificido")
            except FileNotFoundError:
                print("No existe el archivo")

    def filter_by_recognitions(self):
        print("IMPORTANTE: Deben ser solo NUMEROS, (Ej: 10, 20, 2)")
        filter = Menu.validate_int_input("Ingrese los reconocimientos que desea filtrar de los jugadores: ", 0, 50)
        while True:
            try:
                players = self.load_players_json()
#esta primera (jugador_expresion) es una variable de iteracion que se utiliza para recorrer cada elemento de la lista jugadores.
                filter_player = [player_expression for player_expression in players["players"] if player_expression["awards"] == filter]
                if players:
                    print("Jugadores encontrados: ")
                    for player_expression in filter_player:
                        print(json.dumps(player_expression, indent=4))
                    if not self.back_to_menu():
                        break
                else:
                    print("No se encontraron jugadores con los reconocimientos especificidos")
            except FileNotFoundError:
                print("No existe el archivo")

#Visualizar estadisticas jugadores #Visualizar estadisticas jugadores #Visualizar estadisticas jugadores #Visualizar estadisticas jugadores #Visualizar estadisticas jugadores
    def view_player_statistics(self):
        while True:
            name_player = Menu.validate_string_input("Ingrese el nombre del jugador: ")

            players = self.load_players_json()

            player_found = None
            for player in players["players"]:
                if player["name"] == name_player:
                    player_found = player
                    break

            if player_found is None:
                print("El jugador no se encuentra en la base de datos")
                if not self.back_to_menu():
                    break

            print("Estadisticas de ",name_player)
            player_statistics = self.get_player_statistics(player_found)
            print(json.dumps(player_statistics, indent=4))
            if not self.back_to_menu():
                break

    def compare_statistics(self):
        while True:
            name1 = Menu.validate_string_input("Ingrese el nombre del primer jugador: ")
            name2 = Menu.validate_string_input("Ingrese el nombre del segundo jugador: ")

            players = self.load_players_json()

            player1 = None
            player2 = None

            for player in players["players"]:
                if player["name"] == name1:
                    player1 = player
                elif player["name"] == name2:
                    player2 = player

            if player1 is None or player2 is None:
                print("Uno o ambos jugadores no se encontraron, intentelo de nuevo.")
                if not self.back_to_menu():
                    break
                continue

            if player1["position_in_field"] != player2["position_in_field"]:
                print("Los jugadores no poseen la misma posicion de campo y no son comparables")
                if not self.back_to_menu():
                    break
                continue

            print("\nEstadisticas del primer jugador: ")
            player_statistics1 = self.get_player_statistics(player1)
            print(json.dumps(player_statistics1, indent=4))

            print("\nEstadisticas del segundo jugador: ")
            player_statistics2 = self.get_player_statistics(player2)
            print(json.dumps(player_statistics2, indent=4))

            if not self.back_to_menu():
                break
#Gestion de jugadores Gestion de jugadores Gestion de jugadores Gestion de jugadores
    def insert_new_player(self):
        while True:
            # Solicitar al usuario que ingrese los datos del nuevo jugador
            name_player = Menu.validate_string_input("Ingrese el nombre del jugador que desea ingresar (Ej: Lionel Andres Messi): ")

            player_dont_repit_name = self.load_players_json()

            existing_name = False
            for player in player_dont_repit_name["players"]:
                if player.get("name") == name_player:
                    existing_name = True

            if existing_name:
                print("\nError: Este nombre ya esta en uso. Por favor, ingrese un nombre diferente.")
                continue

            while True:
                date_of_birth = input("Ingrese la fecha de nacimiento del jugador (Ej: 28 de octubre de 1991): ")

                # Definir el patron regex para validar la fecha de nacimiento
                patter_date = r"^\d{1,2} de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) de \d{4}$"

                # Verificar si la entrada coincide con el patron regex
                if re.match(patter_date, date_of_birth.lower()):
                    break
                else:
                    print("Error: El formato de la fecha de nacimiento no es válido. Debe ser en el formato 'dd de mes de año'. Por ejemplo, '28 de octubre de 1991'.")

            origin = Menu.validate_string_input("Ingrese el origen del jugador (Ej: Costa Rica): ")

            while True:
                gender = Menu.validate_string_input("Ingrese el género del jugador (Masculino/Femenino/Otro): ")
                if not (gender == "Masculino" or gender == "Femenino" or gender == "Otro"):
                    print("\nError: Debe ser Masculino o Femenino")
                    continue
                else:
                    break

            while True:
                try:
                    height = float(input("Ingrese la altura del jugador (Ej: 1.82) (Min:1.0, Max:2.1 MTS): "))
                    if height < 1.0 or height > 2.1:
                        print("\nError: Debe ser una altura entre 1.0 y 2.1 MTS")
                        continue
                    else:
                        break
                except ValueError:
                    print("Error: Ingrese solo NUMEROS decimales en el formato adecuado (Ej: 1.82)")
                    continue

            while True:
                try:
                    weight = float(input("Ingrese el peso del jugador (Ej: 82.5kgs) (Min:50, Max:130 KGS): "))
                    if weight < 50 or weight > 130:
                        print("\nError: Debe ser un peso entre 50 y 130kgs")
                        continue
                    else:
                        break
                except ValueError:
                    print("Error: Ingrese solo NUMEROS decimales o enteros en el formato adecuado (Ej: 82.5 o 90 KGS)")
                    continue

            position_in_field = Menu.validate_string_input("Ingrese la posición en el campo del jugador (Ej: Delantero): ")
            club_militant = Menu.validate_string_input("Ingrese el club militante del jugador (Ej: Inter Miami): ")
            awards = Menu.validate_int_input("Ingrese los reconocimientos del jugador (Ej: 13): ", 0, 50)

            while True:
                idx = input("Ingrese el ID del jugador (Ej: 30): ")
                if not idx.isdigit():
                    print("\nError: El ID debe ser un número entero.")
                    continue

                players_id_name = self.load_players_json()

                idx = int(idx)
                existing_id = False
                for player in players_id_name["players"]:
                    if player.get("id") == idx:
                        existing_id = True
                        break

                if existing_id:
                    print("\nError: Este ID ya está en uso. Por favor, ingrese un ID diferente.")
                else:
                    break  # El ID es valido y unico

            aceleration = Menu.validate_int_input("Ingrese la aceleracion del jugador (Ej: 42-99): ",42, 99)
            short_passes = Menu.validate_int_input("Ingrese la estadistica de pases cortos del jugador(Ej: 42-99): ", 42, 99)
            power_of_shot = Menu.validate_int_input("Ingrese la potencia de tiro del jugador (Ej: 42-99): ", 42, 99)
            long_passes = Menu.validate_int_input("Ingrese la estadistica de pases largos del jugador(Ej: 42-99): ", 42, 99)
            speed = Menu.validate_int_input("Ingrese la velocidad del jugador(Ej: 42-99): ", 42, 99)
            agility = Menu.validate_int_input("Ingrese la agilidad del jugador(Ej: 42-99): ", 42, 99)
            resistance = Menu.validate_int_input("Ingrese la resistencia del jugador(Ej: 42-99): ", 42, 99)
            jump = Menu.validate_int_input("Ingrese el salto del jugador(Ej: 42-99): ", 42, 99)
            dribbling = Menu.validate_int_input("Ingrese la estadistica de regate del jugador(Ej: 42-99): ",42, 99)
            ball_control = Menu.validate_int_input("Ingrese la estadistica de control de balon del jugador(Ej: 42-99): ", 42, 99)

            # Crear un diccionario con los datos del nuevo jugador
            new_player = {
                "id": idx,
                "name": name_player,
                "date_of_birth": date_of_birth,
                "origin": origin,
                "gender": gender,
                "height": height,
                "weight": weight,
                "position_in_field": position_in_field,
                "club_militant": club_militant,
                "awards": awards,
                "player": player,
                "aceleration": aceleration,
                "short_passes": short_passes,
                "power_of_shot": power_of_shot,
                "long_passes": long_passes,
                "speed": speed,
                "agility": agility,
                "resistance": resistance,
                "jump": jump,
                "dribbling": dribbling,
                "ball_control": ball_control
            }

            # Leer los datos actuales de los jugadores desde el archivo JSON
            try:
                players_insert = self.load_players_json()
                players = players_insert.get("players", [])
            except FileNotFoundError:
                players = []

            # Agregar el nuevo jugador a la lista de jugadores
            players.append(new_player)

            # Escribir los datos actualizados de los jugadores en el archivo JSON
            with open("players_data.json.json", "w") as file:
                json.dump({"players": players}, file, indent=4)

            print("\nNuevo jugador agregado con éxito.")
            if not self.back_to_menu():
                break

    def read_player_information(self):
        while True:
            see_name = self.load_players_json()

            print("\nIMPORTANTE: El NOMBRE del jugador DEBE ser EXACTO (Ej: Lionel Andres Messi)...")
            ask_name = Menu.validate_string_input("Ingrese el nombre del jugador que desea consultar informacion: ")

            existing_name = False
            for player in see_name:
                if player["name"] == ask_name:
                    existing_name = True
# En vez de key y value puede ser cualquier parametro, para mas legibilidad asi, tambien podria ser (for nombre, informacion in jugador.items():
                    print("\nInformacion del jugador:")
                    for key, value in player.items():
                        print(f"{key}: {value}")

            if not existing_name:
                print("\nNo se encontro el jugador que se especifico, intentelo de nuevo...")
                if not self.back_to_menu():
                    break

    def modify_player_data(self):
        while True:
            player_information = self.load_players_json()

            print("\nIMPORTANTE: El NOMBRE del jugador DEBE ser EXACTO (Ej: Lionel Andres Messi)...")

            ask_player_name = Menu.validate_string_input("Ingrese el nombre del jugador que desea modificar: ")

            existing_name = False
            for namee in player_information:
                if namee["name"] == ask_player_name:
                    existing_name = True
                    print("\nInformacion basica del jugador:")
                    print(json.dumps(namee, indent=4))

                    new_name = Menu.validate_string_input("Ingrese el nuevo nombre, si no desea cambiar este dato digite el mismo dato: ")

                    while True:
                        new_date_of_birth = input("Ingrese la nueva fecha de nacimiento, si no desea cambiar este dato digite el mismo dato: ")
                        # Definir el patron regex para validar la fecha de nacimiento
                        pattern_date = r"^\d{1,2} de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) de \d{4}$"

                        # Verificar si la entrada coincide con el patron regex
                        if re.match(pattern_date, new_date_of_birth.lower()):
                            break
                        else:
                            print("Error: El formato de la fecha de nacimiento no es válido. Debe ser en el formato 'dd de mes de año'. Por ejemplo, '28 de octubre de 1991'.")

                    while True:
                        new_gender = input("Ingrese el nuevo genero, si no desea cambiar este dato digite el mismo dato(Masculino/Femenino/Otro): ")
                        if new_gender in ["Masculino", "Femenino", "Otro"]:
                            break
                        else:
                            print("Debe ser exactamente (Masculino/Femenino/Otro), respetando la mayuscula inicial")

                    while True:
                        try:
                            new_height = float(input("Ingrese la nueva altura, si no desea cambiar este dato digite el mismo dato: "))
                            if new_height < 1.0 or new_height > 2.1:
                                print("Error: Ingrese solo NUMEROS, ademas debe ser decimal, con un limite (Min:1.0, Max:2.1 MTS), (Ej: 1.82) : ")
                                continue
                            else:
                                break
                        except ValueError:
                            print("Error: Ingrese solo NUMEROS decimales en el formato adecuado (Ej: 1.82)")
                            continue

                    while True:
                        try:
                            new_weight = float(input("Ingrese el nuevo peso, si no desea cambiar este dato digite el mismo dato: "))
                            if new_weight < 50 or new_weight > 130:
                                print("Error: Ingrese solo NUMEROS, ademas debe ser decimal, con un limite (Min:50, Max:130 KGS), (Ej: 72) : ")
                                continue
                            else:
                                break
                        except ValueError:
                            print("Error: Ingrese solo números decimales en el formato adecuado (Ej: 72, 72.5 KGS)")
                            continue

                    new_position_in_field = Menu.validate_string_input("Ingrese la nueva posicion de campo, si no desea cambiar este dato digite el mismo dato: ")
                    new_militant_club = Menu.validate_string_input("Ingrese el nuevo club militante, si no desea cambiar este dato digite el mismo dato: ")

                    while True:
                        new_awards = input("Ingrese el nuevo(s) reconocimientos, si no desea cambiar este dato digite el mismo dato: ")
                        if not new_awards.isnumeric():
                            print("Error: Debe ser NUMEROS enteros")
                            continue
                        else:
                            new_awards = int(new_awards)
                            break

                    namee["name"] = new_name
                    namee["date_of_birth"] = new_date_of_birth
                    namee["gender"] = new_gender
                    namee["height"] = new_height
                    namee["weight"] = new_weight
                    namee["position_in_field"] = new_position_in_field
                    namee["club_militant"] = new_militant_club
                    namee["awards"] = new_awards

                    with open("players_data.json.json", "w") as informacion_jugadores_file:
                        json.dump(player_information, informacion_jugadores_file, indent=4)

                    print("Los cambios se han aplicado correctamente...")
                    if not self.back_to_menu():
                        break

            if not existing_name:
                print("No se encontro al jugador con el ID y nombre especificados...")

    def remove_player(self):
        while True:
            name_player = Menu.validate_string_input("Ingrese el nombre del jugador que desea eliminar, si desea volver al menu anterior ingrese: ")

            players = self.load_players_json()

            updated_players = [jugador for jugador in players if jugador["nombre"] != name_player]

            if len(updated_players) == len(players):
                print(f"El jugador {name_player} no se encontro en la lista")
                continue

            with open("players_data.json.json", "w") as players_file:
                json.dump(updated_players, players_file, indent=4)

            print(f"El jugador {name_player} se ha eliminado con exito")
            if not self.back_to_menu():
                break

#CONSULTAS AVANZADAS #CONSULTAS AVANZADAS #CONSULTAS AVANZADAS #CONSULTAS AVANZADAS #CONSULTAS AVANZADAS
    def show_number_player_same_origen(self):
        while True:
            search_origin = Menu.validate_string_input("Ingrese el origen para mostrar la cantidad de jugadores: ")
            
            players = self.load_players_json()

            players_same_origin = {}

            for player in players["players"]:
                if player["origin"] == search_origin:
                    if search_origin in players_same_origin:
                        players_same_origin[search_origin] += 1
                    else:
                        players_same_origin[search_origin] = 1

            if search_origin in players_same_origin:
                print(f"La cantidad de jugadores provenientes de {search_origin}: {players_same_origin.get(search_origin, 0)}")
            else:
                print(f"No se encontraron los jugadores provenientes de {search_origin}")
            if not self.back_to_menu():
                break

    def show_all_players_in_an_age_range(self):
        pass

    def show_number_players_with_same_height_and_reference_to_gender_each_one(self):
        pass

    def show_all_players_in_a_specific_club(self):
        while True:
            ask_club = Menu.validate_string_input("Ingrese el nombre del club que desea saber que jugadores pertenecen: ")
            
            players = self.load_players_json()
            players_of_club = []

            for player in players["players"]:
                if player["club_militant"] == ask_club:
                    players_of_club.append(player["name"])

            if players_of_club:
                print(f"El jugadores del club {ask_club} son:")
                for player in players_of_club:
                    print(player)
            else:
                print(f"No se encontraron jugadores del club {ask_club}")
            if not self.back_to_menu():
                break

    def show_number_of_players_accordance_position_on_field_considering_only_gender_female(self):
        while True:
            print("Recuerde son JUGADORAS, en vez de DELANTERO, sera DELANTERA")
            ask_position = Menu.validate_string_input("Ingrese la posicion en el campo(SE CONSIDERA UNICAMENTE EL GENERO FEMENINO): ")

            players = self.load_players_json()

            number_players = 0

            for player in players:
                if player["gender"] == "Femenino" and player["position_in_field"] == ask_position:
                    number_players += 1

            if number_players == 0:
                print(f"No se encontraron jugadores de la posicion {ask_position}")
            else:
                print(f"La cantidad de jugadoras de genero femenino en la posicion de {ask_position} es de: {number_players}")
            if not self.back_to_menu():
                break

    def show_top_ten_players_highest_with_best_agility_information_sample_name_gender_origin_height_agility(self):
        pass

    def show_number_players_whose_speed_is_in_specific_range(self):
        pass

    def determinate_average_ball_control_for_players_in_a_specific_position(self):
        pass

iniciador = Menu()
iniciador.main()