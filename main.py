import mysql.connector
from mysql.connector import errorcode
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
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o contraseña incorrectos!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe!")
        else:
            print(err)

def tabla():
    consulta = "SELECT * FROM alumnos"
    cursor.execute(consulta)
    return cursor.fetchall()

def imprimir_tabla():
    datos = tabla()

    for fila in datos:
        for clave,valor in fila.items():
            print(f"{clave}:{valor}")



def crear_json():
    datos = tabla()
    with open("alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print("archivo 'alumnos.json' creado correctamente")


ConectarBase()
imprimir_tabla()
crear_json()

if cnx.is_connected():
    cnx.close()
    print("La conexión a la base de datos ha sido cerrada.")




