import json
import time
import re
from datetime import datetime

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
            print("5-Mostrar la cantidad de jugadores de acuerdo con la posicion en el campo que posee, considerando UNICAMENTE los de genero femenino")
            print("6-Mostrar el top 10 de los jugadores con mayor altura y con mejor agilidad, la informacion que se muestra es el nombre, genero, origen, altura y agilidad")
            print("7-Mostrar la cantidad de jugadores cuya velocidad este en un rango especifico")
            print("8-Determinar el promedio de control de balon para jugadores en una posicion especifica")
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

    # VALIDACIONES #VALIDACIONES #VALIDACIONES #VALIDACIONES #VALIDACIONES #VALIDACIONES #VALIDACIONES #VALIDACIONES #VALIDACIONES
    def advanced_queries_back(prompt):
        while True:
            user_input = input(prompt)
            if user_input.lower() == "listo":
                break
            else:
                print("Debe colocar estrictamente 'listo'")

    def calculate_age(date_of_birth):
        current_date = datetime.now()
        date_of_birthh = datetime.strptime(date_of_birth, "%d/%m/%Y")
        age = current_date.year - date_of_birthh.year - ((current_date.month, current_date.day) < (date_of_birthh.month, date_of_birthh.day))
        return age

    def validate_gender(prompt):
        while True:
            user_input = input(prompt)
            if not (user_input == "Masculino" or user_input == "Femenino" or user_input == "Otro"):
                print("\nError: Debe ser Masculino/Femenino/Otro")
                continue
            else:
                return user_input

    def validate_position_in_field(prompt):
        while True:
            user_input = input(prompt)
            pattern_position = r"^(Portero|Portera|Defensa|Centrocampista|Defensa Central|Defensa Lateral|Mediapunta|Mediocentro defensivo|Interior Derecho|Interior Izquierdo|Delantero|Delantera|Delantero Centro|Delantera Centro|Segunda Punta|Extremo Izquierdo|Extremo Derecha|Segunda Punta)$"

            if re.match(pattern_position, user_input):
                return user_input
            else:
                print("Error: La posicion ingresada no es valida")
                print("Las posiciones validas son: Portero|Portera|Defensa|Centrocampista|Defensa Central|Defensa Lateral|Mediapunta|Mediocentro defensivo|Interior Derecho|Interior Izquierdo|Delantero|Delantera|Delantero Centro|Delantera Centro|Segunda Punta|Extremo Izquierdo|Extremo Derecha|Segunda Punta")
                continue

    def validate_date_of_birth(prompt):
        while True:
            user_input = input(prompt)
            pattern_birth = r"^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/((19[0-9]{2}|200[0-8]))$"

            if re.match(pattern_birth, user_input):
                try:
                    datetime.strptime(user_input, "%d/%m/%Y")
                    return user_input
                except ValueError:
                    print("Error: La fecha no es valida, debe de usar este formato DIA/MES/AÑO Ej: 10/07/1991 Ademas los dias deben concordar con el mes y esta limitado del AÑO 1900 a 2008")
            else:
                print("Error: La fecha no es valida, debe de usar este formato DIA/MES/AÑO Ej: 10/07/1991, Ademas los dias deben concordar con el mes y esta limitado del AÑO 1900 a 2008. ")

    def validate_string_input_origin(prompt):
        while True:
            user_input = input(prompt)
            words = user_input.split()
            if all(len(word) < 4 for word in words):
                print("Error: El valor minimo deben ser 4 letras, ADEMAS entre cada palabra deben de haber otras 4 (Ej: Costa Rica/Omen )")
                continue
            if not user_input.replace(" ", "").isalpha() or not user_input.istitle():
                print("Error: Deben ser solo letras y empezar con MAYUSCULAS")
                continue
            return user_input

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

    def validate_string_input_min(prompt):
        while True:
            input_string = input(prompt)
            words = input_string.split()
            if not all(len(word) >= 3 for word in words):
                print("Error: Cada palabra debe tener almenos 3 letras")
                continue
            if not input_string.replace(" ", "").isalpha() or not input_string.istitle():
                print("Error: Deben ser solo LETRAS, ademas ambas iniciales deben empezar con MAYUSCULAS")
                continue
            return input_string

    def load_players_json(self):
        try:
            with open("players_data.json", "r") as players_file:
                return json.load(players_file)
        except FileNotFoundError:
            print("El archivo players_data.json no se ha encontrado")
            return None
        except json.decoder.JSONDecodeError:
            print("El archivo players_data.json no contiene datos legibles")
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

    # visualizar_lista_jugadores #visualizar_lista_jugadores #visualizar_lista_jugadores #visualizar_lista_jugadores #visualizar_lista_jugadores
    def filter_by_field_position(self):
        while True:
            print("IMPORTANTE: Deben ser solo LETRAS, ademas ambas iniciales deben empezar con MAYUSCULAS ej: Delantero o Extremo Derecho.")
            position_filter = Menu.validate_string_input("Ingrese la posicion que desea filtrar de los jugadores: ")
            try:
                players = self.load_players_json()
                # esta primera(jugador_expresion)es una variable de iteracion que se utiliza para recorrer cada elemento de la lista jugadores.
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
                # esta primera (jugador_expresion) es una variable de iteracion que se utiliza para recorrer cada elemento de la lista jugadores.
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

    # estadisticas jugadores #estadisticas jugadores #estadisticas jugadores #estadisticas jugadores
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

            print("Estadisticas de ", name_player)
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
    # Gestion de jugadores Gestion de jugadores Gestion de jugadores Gestion de jugadores
    def insert_new_player(self):
        while True:
            # Solicitar al usuario que ingrese los datos del nuevo jugador
            name_player = Menu.validate_string_input_min("Ingrese el nombre del jugador que desea ingresar (Ej: Lionel Andres Messi): ")
            player_dont_repit_name = self.load_players_json()

            existing_name = False
            for player in player_dont_repit_name["players"]:
                if player.get("name") == name_player:
                    existing_name = True
            if existing_name:
                print("\nError: Este nombre ya esta en uso. Por favor, ingrese un nombre diferente.")
                continue

            date_of_birth = Menu.validate_date_of_birth("Ingrese la fecha de nacimiento, debe de usar este formato DIA/MES/AÑO Ej: 25/07/1991: ")
            origin = Menu.validate_string_input_origin("Ingrese el origen del jugador (Ej: Costa Rica): ")
            gender = Menu.validate_gender("Ingrese el género del jugador (Masculino/Femenino/Otro): ")
            height = Menu.validate_float_input("Ingrese la altura del jugador (Ej: 1.82) (Min:1.4, Max:2.1 MTS): ", 1.4,2.1)
            weight = Menu.validate_float_input("Ingrese el peso del jugador (Ej: 82.5kgs) (Min:50, Max:130 KGS): ", 50,130)
            position_in_field = Menu.validate_position_in_field("Ingrese la posición en el campo del jugador (Ej: Delantero): ")
            club_militant = Menu.validate_string_input_min("Ingrese el club militante del jugador (Ej: Inter Miami): ")
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

            aceleration = Menu.validate_int_input("Ingrese la aceleracion del jugador (Ej: 42-99): ", 42, 99)
            short_passes = Menu.validate_int_input("Ingrese la estadistica de pases cortos del jugador(Ej: 42-99): ",42, 99)
            power_of_shot = Menu.validate_int_input("Ingrese la potencia de tiro del jugador (Ej: 42-99): ", 42, 99)
            long_passes = Menu.validate_int_input("Ingrese la estadistica de pases largos del jugador(Ej: 42-99): ", 42,99)
            speed = Menu.validate_int_input("Ingrese la velocidad del jugador(Ej: 42-99): ", 42, 99)
            agility = Menu.validate_int_input("Ingrese la agilidad del jugador(Ej: 42-99): ", 42, 99)
            resistance = Menu.validate_int_input("Ingrese la resistencia del jugador(Ej: 42-99): ", 42, 99)
            jump = Menu.validate_int_input("Ingrese el salto del jugador(Ej: 42-99): ", 42, 99)
            dribbling = Menu.validate_int_input("Ingrese la estadistica de regate del jugador(Ej: 42-99): ", 42, 99)
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
            players = self.load_players_json()

            # Agregar el nuevo jugador a la lista de jugadores
            players["players"].append(new_player)

            # Escribir los datos actualizados de los jugadores en el archivo JSON
            with open("players_data.json", "w") as file:
                json.dump(players, file, indent=4)

            print("\nNuevo jugador agregado con éxito.")
            if not self.back_to_menu():
                break

    def read_player_information(self):
        while True:
            see_name = self.load_players_json()
            print("\nIMPORTANTE: El NOMBRE del jugador DEBE ser EXACTO (Ej: Lionel Andres Messi)...")
            ask_name = Menu.validate_string_input("Ingrese el nombre del jugador que desea consultar informacion: ")

            existing_name = False
            for player in see_name["players"]:
                if player["name"] == ask_name:
                    existing_name = True
                    # En vez de key y value puede ser cualquier parametro, para mas legibilidad asi, tambien podria ser (for nombre, informacion in jugador.items():
                    print("\nInformacion del jugador:")
                    for key, value in player.items():
                        print(f"{key}: {value}")
                    if not self.back_to_menu():
                        return
            if not existing_name:
                print("\nNo se encontro el jugador que se especifico, intentelo de nuevo...")
                if not self.back_to_menu():
                    break

    def modify_player_data(self):
        while True:
            player_information = self.load_players_json()
            players = player_information.get("players", [])

            print("\nIMPORTANTE: El NOMBRE del jugador DEBE ser EXACTO (Ej: Lionel Andres Messi)...")
            ask_player_name = Menu.validate_string_input_min("Ingrese el nombre del jugador que desea modificar: ")

            existing_name = False
            for player in players:
                if player["name"] == ask_player_name:
                    existing_name = True
                    print("\nInformacion basica del jugador:")
                    print(json.dumps(player, indent=4))

                    new_name = Menu.validate_string_input_min("Ingrese el nuevo nombre, si no desea cambiar este dato digite el mismo dato: ")
                    new_date_of_birth = Menu.validate_date_of_birth("Ingrese la nueva fecha de nacimiento, debe de usar este formato DIA/MES/AÑO Ej: 25/07/1991: ")
                    new_gender = Menu.validate_gender("Ingrese el nuevo genero, si no desea cambiar este dato digite el mismo dato(Masculino/Femenino/Otro): ")
                    new_height = Menu.validate_float_input("Ingrese la nueva altura, si no desea cambiar este dato digite el mismo dato: ", 1.4, 2.1)
                    new_weight = Menu.validate_float_input( "Ingrese el nuevo peso, si no desea cambiar este dato digite el mismo dato: ", 50, 130)
                    new_position_in_field = Menu.validate_position_in_field("Ingrese la posición en el campo del jugador (Ej: Delantero): ")
                    new_militant_club = Menu.validate_string_input_min("Ingrese el nuevo club militante, si no desea cambiar este dato digite el mismo dato: ")
                    new_awards = Menu.validate_int_input("Ingrese el nuevo(s) reconocimientos, si no desea cambiar este dato digite el mismo dato: ", 1,100)
                    acceleration = Menu.validate_int_input("Ingrese la nueva estadistica de aceleracion, si no desea cambiar este dato digite el mismo dato: ",42, 99)
                    new_short_passes = Menu.validate_int_input("Ingrese la nueva estadistica de pases cortos, si no desea cambiar este dato digite el mismo dato: ",42, 99)
                    new_power_of_shot = Menu.validate_int_input("Ingrese la nueva estadistica de potencia de tiro, si no desea cambiar este dato digite el mismo dato: ",42, 99)
                    new_long_passes = Menu.validate_int_input("Ingrese la nueva estadistica de pases largos, si no desea cambiar este dato digite el mismo dato: ",42, 99)
                    new_speed = Menu.validate_int_input("Ingrese la nueva estadistica de velocidad, si no desea cambiar este dato digite el mismo dato: ",42, 99)
                    new_agility = Menu.validate_int_input("Ingrese la nueva estadistica de agilidad, si no desea cambiar este dato digite el mismo dato: ",42, 99)
                    new_resistance = Menu.validate_int_input("Ingrese la nueva estadistica de resistencia, si no desea cambiar este dato digite el mismo dato: ",42, 99)
                    new_jump = Menu.validate_int_input("Ingrese la nueva estadistica de salto, si no desea cambiar este dato digite el mismo dato: ",42, 99)
                    new_dribbling = Menu.validate_int_input("Ingrese la nueva estadistica de regate, si no desea cambiar este dato digite el mismo dato: ",42, 99)
                    new_ball_control = Menu.validate_int_input("Ingrese la nueva estadistica de control de balon, si no desea cambiar este dato digite el mismo dato: ",42, 99)

                    player["name"] = new_name
                    player["date_of_birth"] = new_date_of_birth
                    player["gender"] = new_gender
                    player["height"] = new_height
                    player["weight"] = new_weight
                    player["position_in_field"] = new_position_in_field
                    player["club_militant"] = new_militant_club
                    player["awards"] = new_awards
                    player["acceleration"] = acceleration
                    player["short_passes"] = new_short_passes
                    player["power_of_shot="] = new_power_of_shot
                    player["long_passes"] = new_long_passes
                    player["speed"] = new_speed
                    player["agility"] = new_agility
                    player["resistance"] = new_resistance
                    player["jump"] = new_jump
                    player["dribbling"] = new_dribbling
                    player["ball_control"] = new_ball_control

                    with open("players_data.json", "w") as ifile:
                        json.dump({"players": players}, ifile, indent=4)
                    print("Los cambios se han aplicado correctamente...")
                    if not self.back_to_menu():
                        break

            if not existing_name:
                print("No se encontro al jugador con el nombre especificado...")
                if not self.back_to_menu():
                    break

    def remove_player(self):
        while True:
            name_player = Menu.validate_string_input("Ingrese el nombre del jugador que desea eliminar: ")

            players_data = self.load_players_json()
            players = players_data.get("players", [])

            updated_players = [player for player in players if player["name"] != name_player]

            if len(updated_players) == len(players):
                print(f"El jugador {name_player} no se encontro en la lista")
                if not self.back_to_menu():
                    return
            else:

                with open("players_data.json", "w") as players_file:
                    json.dump({"players": updated_players}, players_file, indent=4)
                print(f"El jugador {name_player} se ha eliminado con exito")
                if not self.back_to_menu():
                    break

    # CONSULTAS AVANZADAS #CONSULTAS AVANZADAS #CONSULTAS AVANZADAS #CONSULTAS AVANZADAS #CONSULTAS AVANZADAS
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
        while True:
            players_in_range = []

            players = self.load_players_json()

            min_age = Menu.validate_int_input("Ingrese la edad minima del rango: ", 16, 124)
            max_age = Menu.validate_int_input("Ingrese la edad maximo del rango: ", min_age, 124)

            for player in players["players"]:
                age = Menu.calculate_age(player["date_of_birth"])
                if min_age <= age <= max_age:
                    players_in_range.append(player)

            if players_in_range:
                print("Jugadores en el rango de edad de", min_age, " a ", max_age, "años")
                for player in players_in_range:
                    print(json.dumps(player, indent=4))
                if not self.back_to_menu():
                    return
            else:
                print("No se encontraron los jugadores en el rango de edad de especificado")
                if not self.back_to_menu():
                    return

    def show_number_players_with_same_height_and_reference_to_gender_each_one(self):
        show_players_by_height_and_gender = {}

        players = self.load_players_json()

        for player in players["players"]:
            height = player["height"]
            gender = player["gender"]

            if height not in show_players_by_height_and_gender:
                show_players_by_height_and_gender[height] = {"Masculino": 0, "Femenino": 0, "Otro": 0}

            show_players_by_height_and_gender[height][gender] += 1
        print("Cantidad de jugadores con la misma altura y refentes al genero:")
        for height, gender_counts in show_players_by_height_and_gender.items():
            print(f"Altura{height}m - Masculino: {gender_counts['Masculino']}, Femenino: {gender_counts['Femenino']}, Otro: {gender_counts['Otro']}: ")
        ask = Menu.advanced_queries_back("\nCuando desee volver al menu anterior digite 'listo': ")

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
        players = self.load_players_json()
        sorted_players = sorted(players["players"], key=lambda x: (-x["height"], -x["agility"]))

        print("Los 10 jugadores con mayor altura y agilidad: ")
        for x, player in enumerate(sorted_players[:10], 1):
            print(f"\nPosicion {x}:")
            print(f"Nombre: {player['name']}")
            print(f"Genero: {player['gender']}")
            print(f"Origen: {player['origin']}")
            print(f"Altura: {player['height']}")
            print(f"Agilidad: {player['agility']}")

        ask = Menu.advanced_queries_back("\nCuando desee volver al menu anterior digite 'listo': ")

    def show_number_players_whose_speed_is_in_specific_range(self):
        while True:
            players_speed_range = []
            players = self.load_players_json()

            speed_min = Menu.validate_int_input("Ingrese la velocidad minima del rango: ", 42, 99)
            speed_max = Menu.validate_int_input("Ingrese la velocidad maxima del rango: ", speed_min, 99)

            for player in players["players"]:
                if speed_min <= player["speed"] <= speed_max:
                    players_speed_range.append(player)

            if players_speed_range:
                print("Jugadores con rango de velocidad de", speed_min, "a ", speed_max)
                for player in players_speed_range:
                    print(json.dumps(player, indent=4))
                if not self.back_to_menu():
                    return
            else:
                print("No se encontraron jugadores con ese rango de velocidad")
                if not self.back_to_menu():
                    return

    def determinate_average_ball_control_for_players_in_a_specific_position(self):
        while True:
            players = self.load_players_json()
            specific_position = input("Ingrese la posicion especifica para determinar el promedio de control de balon:")

            total_ball_control_for_players = 0
            num_players = 0

            for player in players["players"]:
                if player["position_in_field"] == specific_position:
                    num_players += 1
                    total_ball_control_for_players += player["ball_control"]

            if num_players == 0:
                print("No hay jugadores en la posicion especificada")
                return

            average_control_ball = total_ball_control_for_players / num_players

            print(f"El promedio de control de balon es de {average_control_ball}")
            if not self.back_to_menu():
                return

iniciator = Menu()
iniciator.main()