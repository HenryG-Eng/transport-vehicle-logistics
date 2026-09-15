# Programa para registrar autos (transportes)

transportes = []  # aquí se van guardando los autos, cada uno es un diccionario


# imprime las opciones del menú, nada más
def mostrar_menu():
    print("\n===== MENÚ - REGISTRO DE TRANSPORTES =====")
    print("1. Registrar datos de transporte")
    print("2. Consultar datos de transporte")
    print("3. Modificar datos de transporte")
    print("4. Salir")
    print("===========================================")


# busca un auto en la lista por su placa, si no está devuelve None
def buscar_por_placa(placa):
    for transporte in transportes:
        if transporte["placa"].lower() == placa.lower():
            return transporte
    return None


# pide los datos de un auto nuevo y lo agrega a la lista
def registrar_transporte():
    print("\n== REGISTRAR TRANSPORTE ==")
    placa = input("Ingrese la placa del transporte: ").strip().upper()

    # no dejamos registrar la misma placa dos veces
    if buscar_por_placa(placa) is not None:
        print(f"Ya existe un transporte registrado con la placa {placa}.")
        return

    nuevo_transporte = {
        "placa": placa,
        "marca": input("Marca: ").strip(),
        "modelo": input("Modelo: ").strip(),
        "año": input("Año: ").strip(),
        "color": input("Color: ").strip(),
        "propietario": input("Propietario: ").strip(),
    }

    transportes.append(nuevo_transporte)
    print(f"Transporte con placa {placa} registrado correctamente.")


# imprime en pantalla los datos de un auto
def mostrar_datos_transporte(transporte):
    print("-" * 35)
    print(f"Placa       : {transporte['placa']}")
    print(f"Marca       : {transporte['marca']}")
    print(f"Modelo      : {transporte['modelo']}")
    print(f"Año         : {transporte['año']}")
    print(f"Color       : {transporte['color']}")
    print(f"Propietario : {transporte['propietario']}")
    print("-" * 35)


# deja elegir entre buscar un auto por placa o ver todos los registrados
def consultar_transporte():
    print("\nCONSULTAR TRANSPORTE")
    print("1. Buscar por placa")
    print("2. Mostrar todos los transportes")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        placa = input("Ingrese la placa a consultar: ").strip().upper()
        transporte = buscar_por_placa(placa)
        if transporte is None:
            print(f"No se encontró ningún transporte con la placa {placa}.")
        else:
            mostrar_datos_transporte(transporte)

    elif opcion == "2":
        if not transportes:
            print("No hay transportes registrados todavía.")
        else:
            print(f"\nHay {len(transportes)} transporte(s) registrado(s):")
            for transporte in transportes:
                mostrar_datos_transporte(transporte)
    else:
        print("Opción no válida.")


# busca un auto por placa y deja cambiar sus datos
def modificar_transporte():
    print("\nMODIFICAR TRANSPORTE")
    placa = input("Ingrese la placa del transporte a modificar: ").strip().upper()
    transporte = buscar_por_placa(placa)

    if transporte is None:
        print(f"No se encontró ningún transporte con la placa {placa}.")
        return

    print("Datos actuales:")
    mostrar_datos_transporte(transporte)

    # si el usuario deja el campo vacío, se queda como estaba
    print("\nDeje el campo vacío si no desea modificarlo.")
    nueva_marca = input(f"Marca [{transporte['marca']}]: ").strip()
    nuevo_modelo = input(f"Modelo [{transporte['modelo']}]: ").strip()
    nuevo_año = input(f"Año [{transporte['año']}]: ").strip()
    nuevo_color = input(f"Color [{transporte['color']}]: ").strip()
    nuevo_propietario = input(f"Propietario [{transporte['propietario']}]: ").strip()

    if nueva_marca:
        transporte["marca"] = nueva_marca
    if nuevo_modelo:
        transporte["modelo"] = nuevo_modelo
    if nuevo_año:
        transporte["año"] = nuevo_año
    if nuevo_color:
        transporte["color"] = nuevo_color
    if nuevo_propietario:
        transporte["propietario"] = nuevo_propietario

    print(f"\nTransporte con placa {placa} actualizado correctamente.")


# ciclo principal, se queda corriendo hasta que el usuario elija salir
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_transporte()
        elif opcion == "2":
            consultar_transporte()
        elif opcion == "3":
            modificar_transporte()
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()