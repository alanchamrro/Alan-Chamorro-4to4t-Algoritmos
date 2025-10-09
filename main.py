
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
        print(suma)

def ejercicio3():
    nuevo_producto = {"nombre": "Escritorio", "precio": 600, "categoria": "Muebles"}
    productos.append(nuevo_producto)
    print(productos)

def ejercicio4():

    productos[2]["precio"] = 400
    print(productos)


def ejercicio5():
        estudiantes = [
            {"nombre": "Ana", "edad": 21, "calificacion": 90},
            {"nombre": "Luis", "edad": 22, "calificacion": 95},
            {"nombre": "Marta", "edad": 20, "calificacion": 85}
        ]

        mayor = estudiantes[0]
        for estudiante in estudiantes:
            if estudiante["calificacion"] > mayor["calificacion"]:
                mayor = estudiante

        print(f"el estudiante con mejor calificación es:{mayor}")

def ejercicio6():

        estudiantes = [
            {"nombre": "Ana", "edad": 21, "calificacion": 90},
            {"nombre": "Luis", "edad": 22, "calificacion": 95},
            {"nombre": "Marta", "edad": 20, "calificacion": 85}
        ]


        nombres = []


        for estudiante in estudiantes:
            nombres.append(estudiante["nombre"])

        print(f"lista de nombres de estudiantes:{nombres}")



def ejercicio7():
    libros = [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
        {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
        {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
    ]


    for libro in libros:
        if libro["titulo"] == "Don Quijote":
            libros.remove(libro)


    print(f"lista después de borrar 'Don Quijote':{libros}")



    libros.append({"titulo": "Don Quijote", "autor": "Miguel de Cervantes"})

    print(f"lista después de volver a añadirlo:{libros}")





def ejercicio8():
    libros = [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
        {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
        {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
    ]

    for libro in libros:
        libro["disponible"] = True

    print("lista de libros con disponibilidad:")
    for libro in libros:
        print(libro)

ejercicio8()








