def ejercicio1():
   plata_inicial = 1000
   while True:
       try:
           elegir = int(input("""
                   1- depositar dinero
                   2- retirar dinero
                   3- salir


                   que desea: """))
       except ValueError:
           print("error: ingrese un numero valido.")
           continue


       if elegir == 1:
           try:
               depositar = int(input("elegi cuanto queres depositar: "))
               plata_inicial += depositar
               print(f"depositaste:",depositar)
               print(f"tu nuevo saldo es:",plata_inicial)
           except ValueError:
               print("error: ingrese un numero valido.")


       elif elegir == 2:
           try:
               retirar = int(input("elegi cuanto queres retirar: "))
               if retirar > plata_inicial:
                   print("no podes retirar mas de lo que tenes.")
               else:
                   plata_inicial -= retirar
                   print(f"retiraste:",retirar)
                   print(f"tu nuevo saldo es:",plata_inicial)
           except ValueError:
               print("error: ingrese un numero valido.")


       elif elegir == 3:
           print("saliendo del programa...")
           break


       else:
           print("elija una opcion valida.")


def ejercicio2():
   while True:
       try:
           peso = float(input("decime tu peso:"))
           altura = float(input("ahora tu altura en metros:"))


           if altura <= 0:
               print("La altura debe ser mayor que 0.")
               continue


           imc = peso / (altura**2)


           if imc < 18.5:
               print(f"tu imc es:", imc)
               print("categoria: bajo peso")


           elif 18.5 <= imc <= 24.9:
               print(f"tu imc es:", imc)
               print("categoria: peso normal")


           elif 25.0 <= imc <= 29.9:
               print(f"tu imc es:", imc)
               print("categoria: sobrepeso")
           elif 30.0 <= imc <= 34.9:
               print(f"tu imc es:", imc)
               print("categoria: obesidad grado 1")


           elif 35.0 <= imc <= 39.9:
               print(f"tu imc es:", imc)
               print("categoria: obesidad grado 2")


           else:
               print(f"tu imc es:", imc)
               print("categoria: obesidad grado 3(morbida)")


       except ValueError:
           print("por favor, ingrese solo números válidos para peso y altura.")

def ejercicio3():

    while True:
        frase = input("escribi una frase (o 'agusfortnite2008' para salir): ")

        if frase == "agusfortnite2008":
            print("programa terminado.")
            break

        for vocal in "aeiou":
            nueva_frase = ""
            for letra in frase:
                if letra in "aeiou":
                    nueva_frase += vocal
                else:
                    nueva_frase += letra
                    print(nueva_frase)




def ejercicio4():
    frase = input("escribi una frase: ")
    palabra = ""
    nueva_frase = ""

    for letra in frase:
        if letra != " ":
            palabra = letra + palabra
        else:
            nueva_frase += palabra + " "
            palabra = ""

    nueva_frase += palabra
    print(nueva_frase)

def ejercicio5():
    nombres = []

    while True:
        print("MENÚ ")
        print("1. Agregar nombre")
        print("2. Mostrar nombre por posición")
        print("3. Salir")

        opcion = input("eligi una opción: ")

        if opcion == "1":
            nombre = input("ingresa un nombre: ")
            nombres.append(nombre)
            print("nombre agregado.")

        elif opcion == "2":
            try:
                pos = int(input("Ingresa el número de posición: "))

                print("El nombre es:", nombres[pos - 1])
            except ValueError:
                print("error: debes ingresar un número.")
            except IndexError:
                print("error: esa posición no existe en la lista.")

        elif opcion == "3":
            print("programa terminado.")
            break

        else:
            print("opción invalida, intentalo de vuelta.")



ejercicio5()


