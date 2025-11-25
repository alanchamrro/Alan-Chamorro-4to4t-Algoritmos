import mysql.connector

import json

cursor = None
cnx = None

def ConectarBase():
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="basededatosconnection20"
        )
        cursor = cnx.cursor(dictionary=True)
        print("Conexión establecida")
    except mysql.connector.Error as err:
        print("Error:", err)



def imprimir_tabla(tabla):
    consulta = f"SELECT * FROM {tabla}"
    cursor.execute(consulta)
    datos = cursor.fetchall()

    for fila in datos:
        for clave, valor in fila.items():
            print(f"{clave}: {valor}")
        print("-" * 20)



def crear_json(tabla):
    consulta = f"SELECT * FROM {tabla}"
    cursor.execute(consulta)
    datos = cursor.fetchall()

    with open(f"{tabla}.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print(f"Archivo '{tabla}.json' creado correctamente")


def imprimir_select(tabla, columnas):
    columnas_str = ", ".join(columnas)
    consulta = f"SELECT {columnas_str} FROM {tabla}"
    cursor.execute(consulta)
    datos = cursor.fetchall()

    for fila in datos:
        for clave, valor in fila.items():
            print(f"{clave}: {valor}")
        print("-" * 20)


def modificar_campo(tabla, campo, nuevo_valor, id_registro):
    consulta = f"UPDATE {tabla} SET {campo} = %s WHERE id = %s"
    cursor.execute(consulta, (nuevo_valor, id_registro))
    cnx.commit()
    print("Registro actualizado correctamente")



def insertar_datos(nombre, edad, año, correo):
    consulta = "INSERT INTO alumnos (nombre, edad, año, correo) VALUES (%s, %s, %s, %s)"
    valores = (nombre, edad, año, correo)
    cursor.execute(consulta, valores)
    cnx.commit()
    print("Datos insertados correctamente")



def menu():
    while True:
        print("""
 MENÚ
1. Imprimir tabla completa
2. Crear archivo JSON
3. SELECT personalizado
4. Modificar valor (UPDATE)
5. Insertar nuevo alumno
6. Salir
""")

        op = input("Elegí opción: ")

        if op == "1":
            imprimir_tabla("alumnos")

        elif op == "2":
            crear_json("alumnos")

        elif op == "3":
            columnas = input("Ingresá columnas separadas por coma (ej: nombre,edad): ")
            columnas = [c.strip() for c in columnas.split(",")]
            imprimir_select("alumnos", columnas)

        elif op == "4":
            campo = input("Campo a modificar (nombre, edad, año, correo): ")
            nuevo = input("Nuevo valor: ")
            id_reg = int(input("ID del alumno a modificar: "))
            modificar_campo("alumnos", campo, nuevo, id_reg)

        elif op == "5":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            año = int(input("Año: "))
            correo = input("Correo: ")
            insertar_datos(nombre, edad, año, correo)

        elif op == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


ConectarBase()
menu()

if cnx.is_connected():
    cnx.close()
    print("Conexión cerrada.")

