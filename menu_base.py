#<<<<<<< rama_esteban
# Menú base del progam

def datos_esteban():
    print("Mi nombre es Esteban Gonzalez y tengo 31 años.")
=======
# Menú base del programa
def info_javier() :
    print("Mi nombre es Javier Jara y tengo 29 años")
#>>>>>>> main
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        info_javier()
    elif op == "2":
        datos_esteban()
    elif op == "3":
        pass # Aquí se llamará a la función del integrante 3
    else:
        print(" Opción inválida.")
