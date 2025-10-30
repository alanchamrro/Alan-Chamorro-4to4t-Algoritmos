import json
#guia de ejercicios 16---

def ejercicio1():
    informacion_personal = {
        "nombre": "alan",
        "edad": 17,
        "ciudad": "new york",
        "profesion": "estudiante"
    }
    print(informacion_personal)

    with open("Ejercicio1.json", "w", encoding="utf-8") as archivo:
        json.dump(informacion_personal, archivo, indent=4, ensure_ascii=False)


def ejercicio2():
    informacion_personal = {
        "nombre": "alan",
        "edad": 17,
        "ciudad": "new york",
        "profesion": "nada"
    }

    informacion_personal["ciudad"] = "buenos aires"
    informacion_personal["profesion"] = "estudiante"
    informacion_personal["telefono"] = 1165844664
    informacion_personal["mail"] = "alan.chamorroet32@gmail.com"

    print(informacion_personal)

    with open("Ejercicio2.json", "w", encoding="utf-8") as archivo:
        json.dump(informacion_personal, archivo, indent=4, ensure_ascii=False)


def ejercicio3():
    calificaciones = {
        "matematicas": 8,
        "lengua": 7,
        "Ciencias": 5
    }
    print(calificaciones["matematicas"])

    with open("Ejercicio3.json", "w", encoding="utf-8") as archivo:
        json.dump(calificaciones, archivo, indent=4, ensure_ascii=False)


def ejercicio4():
    calificaciones = {
        "matematicas": 8,
        "lengua": 7,
        "Ciencias": 5
    }

    promedio = sum(calificaciones.values()) / len(calificaciones)
    print(promedio)

    with open("Ejercicio4.json", "w", encoding="utf-8") as archivo:
        json.dump({"calificaciones": calificaciones, "promedio": promedio}, archivo, indent=4, ensure_ascii=False)


def ejercicio5():
    paises_capitales = {
        "argentina": "buenos aires",
        "españa": "madrid",
        "mexico": "ciudad de mexico"
    }

    with open("Ejercicio5.json", "w", encoding="utf-8") as archivo:
        json.dump(paises_capitales, archivo, indent=4, ensure_ascii=False)

    while True:
        elegir = int(input("""ingresá un pais en el que quieras saber la capital
                  1-argentina
                  2-españa
                  3-mexico
                  :"""))

        if elegir == 1:
            print(paises_capitales["argentina"])
        elif elegir == 2:
            print(paises_capitales["españa"])
        elif elegir == 3:
            print(paises_capitales["mexico"])
        else:
            print("elegi un pais valido")


def ejercicio6():
    precios = {
        "pan": 150,
        "leche": 300,
        "arroz": 250,
        "huevos": 500
    }

    def costo_total(producto, cantidad):
        if producto in precios:
            return precios[producto] * cantidad
        else:
            return "producto no disponible"

    print(costo_total("pan", 3))
    print(costo_total("leche", 2))
    print(costo_total("carne", 1))

    with open("Ejercicio6.json", "w", encoding="utf-8") as archivo:
        json.dump(precios, archivo, indent=4, ensure_ascii=False)


def ejercicio7():
    informacion_personal = {
        "nombre": "alan",
        "edad": 17,
        "ciudad": "new york",
        "profesion": "estudiante",
        "telefono": 1165844664
    }

    del informacion_personal["telefono"]

    print(informacion_personal)

    with open("Ejercicio7.json", "w", encoding="utf-8") as archivo:
        json.dump(informacion_personal, archivo, indent=4, ensure_ascii=False)


def ejercicio8():
    dic = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    print(dic.get("a"))
    print(dic.get("z"))

    with open("Ejercicio8.json", "w", encoding="utf-8") as archivo:
        json.dump(dic, archivo, indent=4, ensure_ascii=False)


def ejercicio9():
    dic = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    dic2 = {
        "d": 4,
        "f": 5,
        "g": 3
    }

    dic3 = dic | dic2

    print(dic3)

    with open("Ejercicio9.json", "w", encoding="utf-8") as archivo:
        json.dump(dic3, archivo, indent=4, ensure_ascii=False)

#guia de ejercicios 17--


import json

productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
    {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
    {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
]

def ejercicio1():
    for producto in productos:
        print(producto['nombre'])

def ejercicio2():
    suma = 0
    for producto in productos:
        suma += producto['precio']
    print("Suma total de precios:", suma)

def ejercicio3():
    nuevo_producto = {"nombre": "Escritorio", "precio": 600, "categoria": "Muebles"}
    productos.append(nuevo_producto)
    print("Lista de productos actualizada:")
    print(productos)

  
    with open("CHECHON.json", "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)
    print("Archivo CHECHON.json creado correctamente ✅")

def ejercicio4():
    productos[2]["precio"] = 400
    print("Lista de productos con precio modificado:")
    print(productos)


    with open("CHECHON.json", "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)
    print("Archivo CHECHON.json actualizado correctamente ✅")





