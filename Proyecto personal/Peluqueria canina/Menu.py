def mostrar_menu():
    print("\n🐾 PELUQUERÍA CANINA 🐾")
    print("========================")
    print("1. Baño y secado")
    print("2. Baño + corte")
    print("3. Corte y arreglo")
    print("4. Higiene")
    print("5. Deslanado")
    print("6. Spa canino")
    print("7. Sacar turno")
    print("8. Consultar precios")
    print("9. Ver horarios")
    print("0. Salir")
    print("========================")


while True:
    mostrar_menu()

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print("🐶 Servicio seleccionado: Baño y secado")

    elif opcion == "2":
        print("✂️ Servicio seleccionado: Baño + corte")

    elif opcion == "3":
        print("✨ Servicio seleccionado: Corte y arreglo")

    elif opcion == "4":
        print("🧼 Servicio seleccionado: Higiene")

    elif opcion == "5":
        print("🐕 Servicio seleccionado: Deslanado")

    elif opcion == "6":
        print("🛁 Servicio seleccionado: Spa canino")

    elif opcion == "7":
        print("📅 Sacar turno")

    elif opcion == "8":
        print("💰 Consultar precios")

    elif opcion == "9":
        print("🕐 Horarios: Lunes a Sábado de 9:00 a 18:00")

    elif opcion == "0":
        print("¡Gracias por visitar nuestra peluquería! 🐾")
        break

    else:
        print("❌ Opción inválida. Intentá nuevamente.")