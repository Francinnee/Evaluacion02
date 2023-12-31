#Ejercicio

class MenuPrincipal:
    #se inicializan las variables de la clase
    def __init__(self):
        self.compras = []
        self.total_gastado = 0

    #se agregan los montos de compra de los clientes, opcion 1
    def agregar_compra(self):
        monto = float(input("Ingrese el monto de la compra: "))
        self.compras.append(monto) #agrega el monto al final de la fila
        self.total_gastado += monto
        print("Compra agregada correctamente.")

    #se muestran las compras registradas
    def mostrar_compras(self):
        if not self.compras:
            print("No hay compras registradas.")
        else:
            for i, monto in enumerate(self.compras, start=1): #recibe un objeto y retorna tuplas
                print(f"Compra {i}: ${monto:.2f}")

    #se muestra el total de gastado
    def mostrar_total(self):
        print(f"Total gastado: ${self.total_gastado:.2f}")

    #se crea una lista de las opciones
    def main(self):
        while True:
            print("\nMenu:")
            print("1. Agregar compra")
            print("2. Mostrar compras")
            print("3. Mostrar total gastado")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_compra()
            elif opcion == "2":
                self.mostrar_compras()
            elif opcion == "3":
                self.mostrar_total()
            elif opcion == "4":
                print("Hasta luego :D!")
                break
            else:
                print("Opción no válida. Por favor, elija una opción del 1 al 4.")

app = MenuPrincipal()
app.main()
