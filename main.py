from Aerolinea import Aerolinea
from Pasajero import Pasajero, PasajeroEconomico, PasajeroEjecutivo, PasajeroPremium
from Vuelo import Vuelo
from Tiquete import Tiquete
from CargaEspecial import Bicicleta, Mascota




def main():
    aerolinea = Aerolinea()

    
    

    

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear vuelo")
        print("2. Vender tiquete")
        print("3. Hacer check-in")
        print("4. Devolver tiquete")
        print("5. Estadísticas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            origen = input("Ciudad de origen: ")
            destino = input("Ciudad de destino: ")
            aerolinea.crear_vuelo(origen, destino)
            print("Vuelo creado con éxito.")
            

        elif opcion == "2":
            if not aerolinea.vuelos:
                print("No hay vuelos disponibles.")
                continue
            print("Vuelos disponibles:")
            for i, vuelo in enumerate(aerolinea.vuelos):
                print(f"{i+1}. {vuelo.origen} -> {vuelo.destino}")
            try:
                index = int(input("Seleccione el número de vuelo: ")) - 1
                vuelo = aerolinea.vuelos[index]
                nombre = input("Nombre del pasajero: ")
                edad = int(input("Edad del pasajero: "))
                genero = input("Género (masculino/femenino): ")
                clase = input("Clase (economica/ejecutiva/premium): ").lower()
                valor = float(input("Valor base del tiquete: "))
                pasajero = Pasajero(nombre, edad, genero)
                tiquete = vuelo.vender_tiquete(pasajero, clase, valor)

                while True:
                    agregar = input("¿Agregar carga especial? (s/n): ").lower()
                    if agregar == "n":
                        break
                    tipo = input("Tipo (bicicleta/perro/gato): ").lower()
                    if tipo == "bicicleta":
                        peso = float(input("Peso de la bicicleta (kg): "))
                        tarifa = float(input("Tarifa por kilo: "))
                        carga = Bicicleta(peso, tarifa)
                    else:
                        carga = Mascota(tipo)
                    tiquete.pasajero.agregar_carga_especial(carga)

                print("Tiquete vendido con éxito.")
            except Exception as e:
                print("Error:", e)

        elif opcion == "3":
            if not aerolinea.vuelos:
                print("No hay vuelos.")
                continue
            for i, vuelo in enumerate(aerolinea.vuelos):
                print(f"{i+1}. {vuelo.origen} -> {vuelo.destino}")
            try:
                index = int(input("Seleccione el número de vuelo: ")) - 1
                vuelo = aerolinea.vuelos[index]
                if not vuelo.tiquetes:
                    print("No hay tiquetes vendidos para este vuelo.")
                    continue
                for j, tiquete in enumerate(vuelo.tiquetes):
                    print(f"{j+1}. {tiquete.pasajero.nombre} - {tiquete.clase}")
                t_index = int(input("Seleccione el número de tiquete: ")) - 1
                tiquete = vuelo.tiquetes[t_index]
                peso = float(input("Peso del equipaje: "))
                total_costo = vuelo.check_in(tiquete, peso)
                print("Costo adicional por equipaje/cargas especiales:", total_costo)
            except Exception as e:
                print("Error:", e)

        elif opcion == "4":
            if not aerolinea.vuelos:
                print("No hay vuelos.")
                continue
            for i, vuelo in enumerate(aerolinea.vuelos):
                print(f"{i+1}. {vuelo.origen} -> {vuelo.destino}")
            try:
                index = int(input("Seleccione el número de vuelo: ")) - 1
                vuelo = aerolinea.vuelos[index]
                if not vuelo.tiquetes:
                    print("No hay tiquetes para devolver.")
                    continue
                for j, tiquete in enumerate(vuelo.tiquetes):
                    print(f"{j+1}. {tiquete.pasajero.nombre}")
                t_index = int(input("Seleccione el tiquete a devolver: ")) - 1
                vuelo.devolver_tiquete(vuelo.tiquetes[t_index])
                print("Tiquete devuelto con éxito.")
            except Exception as e:
                print("Error:", e)

        elif opcion == "5":
            print("--- ESTADÍSTICAS ---")
            t = aerolinea.trayecto_mayor_recaudo()
            if t:
                print(f"Trayecto con mayor recaudo: {t[0]} -> {t[1]}, Total: {t[2]}")
            else:
                print("No hay trayectos registrados.")
            destino = input("Destino para análisis de género: ")
            print("Viajan más:", aerolinea.quienes_viajan_mas(destino))
            o = input("Origen para promedio: ")
            d = input("Destino para promedio: ")
            print("Costo promedio tiquete:", aerolinea.costo_promedio_tiquete(o, d))
            print("Recaudo total por tiquetes:", aerolinea.recaudo_total_tiquetes())
            print("Recaudo total por equipaje/cargas especiales:", aerolinea.recaudo_total_equipaje())
        
        elif opcion == "6":
                print("Saliendo del sistema...")
                break
        
       

        else:
            print("Opción inválida. Intente nuevamente.")


main()













