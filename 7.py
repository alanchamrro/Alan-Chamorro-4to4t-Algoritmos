import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rubricasdb"
    )



def crear_rubrica():
    cnx = conectar()
    cursor = cnx.cursor()

    nombre = input("Ingrese nombre de la nueva rúbrica: ")
    cursor.execute("INSERT INTO rubricas (nombre) VALUES (%s)", (nombre,))
    cnx.commit()
    cnx.close()

    print("Rúbrica creada correctamente.")



def agregar_criterios():
    cnx = conectar()
    cursor = cnx.cursor()

    id_rubrica = int(input("ID de la rúbrica a la cual agregar criterios: "))

    while True:
        nombre = input("Nombre del criterio: ")
        puntaje = int(input("Puntaje máximo (ej: 10): "))

        cursor.execute("""
            INSERT INTO criterios (id_rubrica, nombre, puntaje_maximo)
            VALUES (%s, %s, %s)
        """, (id_rubrica, nombre, puntaje))

        cnx.commit()

        seguir = input("¿Agregar otro criterio? (si/no): ")
        if seguir != "si":
            break

    cnx.close()
    print("Criterios agregados correctamente.")




def listar_rubricas():
    cnx = conectar()
    cursor = cnx.cursor()

    cursor.execute("SELECT id, nombre FROM rubricas")
    datos = cursor.fetchall()

    print(" LISTA DE RÚBRICAS ")
    for r in datos:
        print(f"{r[0]} - {r[1]}")
    print("")

    cnx.close()



def mostrar_criterios():
    cnx = conectar()
    cursor = cnx.cursor()

    id_rubrica = int(input("Ingrese ID de la rúbrica: "))

    cursor.execute("""
        SELECT criterios.nombre, criterios.puntaje_maximo
        FROM criterios
        WHERE id_rubrica = %s
    """, (id_rubrica,))

    datos = cursor.fetchall()

    print("CRITERIOS DE LA RÚBRICA")
    for c in datos:
        print(f"Criterio: {c[0]} | Puntaje máximo: {c[1]}")
    print("")

    cnx.close()



def menu():
    while True:
        print("""
 MENÚ 

1) Crear nueva rúbrica
2) Agregar criterios a una rúbrica
3) Listar rúbricas
4) Mostrar criterios de una rúbrica
5) Salir


""")

        op = input("Elige una opción: ")

        if op == "1":
            crear_rubrica()
        elif op == "2":
            agregar_criterios()
        elif op == "3":
            listar_rubricas()
        elif op == "4":
            mostrar_criterios()
        elif op == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


menu()